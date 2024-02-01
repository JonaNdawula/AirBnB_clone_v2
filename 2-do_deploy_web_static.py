#!/usr/bin/python3
"""
A Fabric script that
distributes an archive
to my web servers
"""
import os
from datetime import datetime
from fabric.api import *

env.hosts = ["100.25.4.139", "54.90.24.175"]
env.user = "ubuntu"


def do_pack():
    """
    Returns archive file
    """

    local("mkdir -p versions")
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    arch_file_path = f"versions/web_static_{date_time}.tgz"
    gzip_arch = local("tar -cvzf {} web_static".format(arch_file_path))

    if gzip_arch.succeeded:
        return arch_file_path
    else:
        return None


def do_deploy(archive_path):
    """
    Distributes the archive
    """
    if os.path.exists(archive_path):
        file_arch = archive_path[9:]
        new_version = "/data/web_static/releases/" + file_arch[:-4]
        file_arch = "/tmp/" + file_arch
        put(archive_path, "/tmp/")
        run(f"sudo mkdir -p {new_version}")
        run(f"sudo tar -xzf {file_arch} -C {new_version}/")
        run(f"sudo rm {file_arch}")
        run(f"sudo mv {new_version}/web_static/* {new_version}")
        run(f"sudo rm -rf {new_version}/web_static")
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {new_version} /data/web_static/current")

        print("New version deployed!")
        return True

    return False
