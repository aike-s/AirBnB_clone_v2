#!/usr/bin/env bash
# Set up my web servers for the deployment of web_static
apt-get -y update
apt-get -y install nginx

# Create the folders if they doesn't exist
mkdir -p data
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

# Create fake HTML file
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>">/data/web_static/releases/test/index.html

# Create a symlink
ln -sfn /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu:ubuntu /data/

# Config nginx to serve the content of /data/web_static/current/ to hbnb_static
add_config="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "42i $add_config" /etc/nginx/sites-available/default

service nginx restart
