#!/usr/bin/python3
"""Fabric script that distributes an archive
to your web servers, using the function do_deploy"""

from fabric.api import local, put, env, run
from os import path
from datetime import datetime
env.hosts = ['34.229.91.198', '54.234.82.120']
env.user = "ubuntu"


def do_pack():
    """Compress before sending"""
    local("mkdir -p versions")
    # create the name of file in str format from datetime.now
    name = "web_static_" + datetime.strftime(datetime.now(),
                                             "%Y%m%d%H%M%S") + ".tgz"
    try:
        local("tar -czvf ./versions/{} ./web_static" .format(name))
        return(name)
    except:
        return(None)


def do_deploy(archive_path):
    """function to distribute an archive to web server"""
    if not (path.exists(archive_path)):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split('/')[1].split('.')[0]
        run("sudo mkdir -p /data/web_static/releases/{}".format(name))
        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}"
            .format(name, name))
        run("sudo rm /tmp/{}.tgz".format(name))
        run("sudo mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))
        return True
    except:
        return False


def deploy():
    """Compress and upload files to remote server."""
    path = do_pack()
    print(path)
    if path is None:
        return False
    deploy = do_deploy(path)
    if deploy is False:
        return False
    return deploy
