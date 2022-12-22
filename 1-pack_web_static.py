#!/usr/bin/python3
"""Fabric script that generates a .tgz archive
    from the contents of the web_static folder
"""

from fabric.api import local
from datetime import datetime
from fabric.decorators import runs_once


@runs_once
def do_pack():
    """Generating .tgz archive from the contents of a folder"""
    local("mkdir -p versions")
    date = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    path = ("versions/web_static_{}.tgz".format(date))
    output = local("tar -cvzf {} web_static".format(path))

    if out.failed:
        return None
    return path
