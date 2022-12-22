#!/usr/bin/python3
"""
    Fabric script that distributes an archive to web servers
"""

import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once
from fabric.decorator import runs_once

env.hosts = ['52.86.124.17', '18.234.80.128']
env.user = "ubuntu"


@runs_once
def do_pack():
    """Generating .tgz archive from the contents of a folder"""
    local("mkdir -p versions")
    date = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    path = ("versions/web_static_{}.tgz".format(date))
    output = local("tar -cvzf {} web_static".format(path))

    if output.failed:
        return None
    return path


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
        Args:
            archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False

    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
