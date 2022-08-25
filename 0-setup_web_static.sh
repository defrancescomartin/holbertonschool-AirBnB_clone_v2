#!/usr/bin/env bash
# Web servers set up for deployment of web static

#nginx installation (already installed)
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

#folder creation
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

sudo touch /data/web_static/releases/test/index.html #html creation
echo "
<html>
 <head>
   <title>
   Holberton School (title)
   </title>
 </head>

 <body>
   Holberton School (body)
 </body>
 </html>" > sudo /data/web_static/releases/test/index.html

sudo ln -sfn /data/web_static/releases/test/ /data/web_static/current #Symlink

sudo chown -R ubuntu:ubuntu /data/ #Ownership creation

sudo sed -i '/listen 80 default_server/a location /hbnb_static/ {alias /data/web_static/current/;}' /etc/nginx/sites-available/default #nginx setup

sudo service nginx restart #save changes and restart the service
