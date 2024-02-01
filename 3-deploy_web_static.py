#!/usr/bin/python3
"""
"""
import os.path
from datetime import datetime
from fabric.api import env, put, run, local


env.hosts = ["100.25.4.139", "54.90.24.175"]


def do_pack():
    """
    """
    date_time = datetime.utcnow()
    myfile = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(myfile)).failed is True:
        return None
    return myfile



def do_deploy(archive_path):
    """
    Distributes archive to
    web server
    """
    if os.path.isfile(archive_path) is False:
        return False
    myfile = archive_path.split("/")[-1]
    f_name = myfile.split(".")[0]

    if put(archive_path, "/tmp/{}".format(myfile)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(f_name)).failed is True:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".
           format(f_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(myfile, f_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(myfile)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(f_name, f_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(f_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(f_name)).failed is True:
        return False
    return True

def deploy():
    """
    Distibutes archive
    to web servers
    """
    f = do_pack()
    if f is None:
        return False
    return do_deploy(f)
