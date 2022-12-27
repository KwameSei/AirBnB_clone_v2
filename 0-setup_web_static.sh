#!/usr/bin/env bash
# Script that sets up web servers for the deployment of web_static

# Update packages
sudo apt-get update
sudo apt-get install nginx -y

# Create directories
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Creating a test file
echo "Welcome my buddy! Come back for an exciting news soon" | sudo tee /data/web_static/releases/test/index.html

SERVER_BLOCK=\
server {
	listen 80 default_server;
	listen [::]:80 default_server;
	server_name nathanielosei.tech www.nathanielosei.tech

	root /var/www/html;
	index index.html index.htm index.nginx-debian,html;

	add_header X-Served-By $hostname;

	error_page 404 /404.html;
	location = /404.html {
		internal;
	}

	location /redirect_me {
		return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
	}

	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
echo SERVER_BLOCK | sudo tee /etc/nginx/sites-available/default

# Prevent overwriting
sudo rm -rf /etc/nginx/sites-enabled/

# Creating symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Change ownership
sudo chown -hR ubuntu:ubuntu /data

#updating nginx to serve content
sudo ln -sf /etc/nginx/sites-available /etc/nginx/sites-enabled

#restarting nginx
sudo service nginx restart
