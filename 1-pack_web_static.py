#!/usr/local/lib/python3
"""Fabric script that generates a .tgz archive
    from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generating .tgz archive from the contents of a folder"""
    folder = 'web_static'
    # Create the versions folder if it doesn't exist
    new_dir = local('mkdir -p versions')
    new_dir = 'versions'

    # Get the current date and time
    date = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    filename = "{}_{}.tgz".format(folder, date)

    path = ("{}/{}".format(new_dir, filename))
    # Create the .tgz archive
    result = local("tar -cvzf {} {}".format(path, folder))

    if result.succeeded:
        #return result
        return path
    #else:
        #return None
    # Move the .tgz archive to the "versions" folder
    #local("mv {} {}".format(filename, new_dir))
    return None
