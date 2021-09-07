#!/usr/bin/python3
from genericpath import exists
from fabric.api import local, run, env, put
import time
from os import path
env.hosts = ['3.91.5.156', '34.228.153.16']
env.user = 'ubuntu'


def do_pack():
    """ Generates a .tgz archive from the contents of the web_static folder """

    file_name = "web_static_{}.tgz".format(time.strftime("%Y%m%dT%H%M%S"))

    local('mkdir -p versions')
    try:
        local('tar -czvf versions/' + file_name + ' web_static/*')
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """

    if not path.exists(archive_path):
        return False

    file_name = archive_path[9:-4]
    dir_name = "/data/web_static/releases/{}/".format(file_name)

    try:
        """ Upload tar archive """
        put(archive_path, '/tmp/')

        """ Uncompress the archive to a specific folder """
        run('sudo mkdir -p ' + dir_name)
        run('sudo tar -xzf /tmp/{}.tgz -C {}'.format(file_name, dir_name))

        """ Delete the archive from the web server """
        run('sudo rm /tmp/{}.tgz'.format(file_name))

        """ Move info """
        run('sudo mv {}/web_static/* {}'.format(dir_name, dir_name))

        """ Delete the symbolic link """
        run('sudo rm -rf /data/web_static/current')

        """ Create a new symbolic link """
        run('sudo ln -sf {} /data/web_static/current'.format(dir_name))

        return True

    except:
        return False


def do_deploy():
    """  """

    created_file = do_pack()
    path = "versions/{}".format(created_file)

    if not path.exists(path):
        return False

    answer = do_deploy(path)

    return answer


def do_clean(number=0):
    """  """

    