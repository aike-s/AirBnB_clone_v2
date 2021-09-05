#!/usr/bin/python3import time
from fabric.api import local, run
import time


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder """

    file_name = "web_static_{}.tgz".format(time.strftime("%Y%m%dT%H%M%S"))

    local('mkdir -p versions')
    try:
        local('tar -czvf versions/' + file_name + ' web_static/*')
        return file_name
    except:
        return None
