#!/usr/bin/python3
# Generates a .tgz archive from the contents of the web_static folder
import time
from fabric.api import local, run

def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder """

    file_name = "web_static_{}.tgz".format(time.strftime("%Y%m%dT%H%M%S"))

    local('mkdir -p versions')
    result = run('tar -xf versions/' + file_name + 'jweb_static/*')

    if result.succeeded:
        return local('realpath' + file_name)
    else:
        None
