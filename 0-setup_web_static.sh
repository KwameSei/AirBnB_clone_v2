#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Update packages
sudo apt-get update
sudo apt-get install nginx -y
echo -e "\e[1;32m Packages updated\e[0m"
echo

# Configuring firewall
sudo ufw allow 'Nginx HTTP'

# Create directories
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo "<h2>Welcome to $hostname's Web Page</h1>" > /data/web_static/releases/test/index.html

echo "server {
	listen 80 default_server;
	root /var/www/html;
	index index.html index.htm index.nginx-debian,html;
	server_name _;
	add_header X-Served-By $hostname;
	location / {
		try_files $uri $uri/ =404;
	}
	if ($request_filename ~ redirect_me) {
		rewrite ^ https://youtube.com permanent;
	}
	error_page 404 /404.html;
	location = /404.html {
		internal;
	}
	location /hbnb_static/ {
		alias /data/web_static/current/;
	}
}" / sudo tee /etc/nginx/sites-available/default

# Prevent Overwriting
if [ -d "/data/web_static/current" ];
then
	echo "path /data_web_static/current exists"
	sudo rm -rf /data/web_static/current;
fi;

# Creating symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

#updating nginx to serve content
sudo ln -sf '/etc/nginx/sites-available/default' '/etc/nginx/sites-enabled/default'

#restarting nginx
sudo service nginx restart
