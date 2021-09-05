#!/usr/bin/env bash
# Set up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx

# Create the folders if they doesn't exist

sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# Create fake HTML file
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create a symlink
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Config nginx to serve the content of /data/web_static/current/ to hbnb_static
search="server_name _;"
add_config="location /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sudo sed -i "/$search/a\\$add_config" /etc/nginx/sites-available/default

sudo service nginx restart
