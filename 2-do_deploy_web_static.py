#!/usr/bin/python3
"""
    Fabric script that distributes an archive to web servers
"""
import os
from datetime import datetime
from fabric.api import env, local, put, run, runs_once

# Set the environment variables for the server(s) to deploy to
env.user = "ubuntu"
env.hosts = ['52.86.124.17', '18.234.80.128']


def do_pack():
    """Generating .tgz archive from the contents of a folder"""
    folder = 'web_static'
    # Create the versions folder if it doesn't exist
    new_dir = local('mkdir -p versions')
    new_dir = 'versions'

    if not os.path.isdir(new_dir):
        os.mkdir(new_dir)

    # Get the current date and time
    date = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    filename = "{}_{}.tgz".format(folder, date)

    path = ("{}/{}".format(new_dir, filename))
    # Create the .tgz archive

    try:
        print("Packing web_static to {}".format(path))
        local("tar -cvzf {} {}".format(path, folder))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(path, archize_size))
    except Exception:
        path = None
    return path


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
        Args:
        archive_path (str): The path to the archived static files.
    """

    # Return False if the file at the path archive_path doesn’t exist
    if not os.path.exists(archive_path):
        return False

    # Traversing the file path to find the filename
    file_name = os.path.basename(archive_path)
    # Setting the folder name to the filename without the file extension
    folder_name = file_name.replace(".tgz", "")
    # Path to the folder created
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False

    try:
        # Upload the archive to the server(s)
        put(archive_path, "/tmp/{}".format(file_name))
        # Creating a folder at /data/web_static/releases/folder_name/
        run("mkdir -p {}".format(folder_path))
        # Extract the archive and move the contents to the web root directory
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        # Delete the archive from the web server
        run("rm -rf /tmp/{}".format(file_name))
        # Move the extracted files to the desired folder
        run("mv {}web_static/* {}".format(folder_path, folder_path))

        run("rm -rf {}web_static".format(folder_path))
        # Delete the symbolic link /data/web_static/current
        run("unlink /data/web_static/current")
        """ Create a new symbolic link /data/web_static/current,
        linked to the new version of your code """
        run("ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
