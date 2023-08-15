#!/usr/bin/python3
"""Distributes archive to web server using fabric"""

from fabric.api import env, put, run, sudo
from os.path import exists

env.hosts = ['100.25.188.21', '52.86.207.199']


def do_deploy(archive_path):
    """Deploys zipped file to server location"""
    if exists(archive_path):
        try:
            archive_file = archive_path.split("/")[-1]
            no_ext = archive_file.split(".")[0]
            path = '/data/web_static/releases/'
            put(archive_path, '/tmp/')
            run("mkdir -p {}{}/".format(path, no_ext))
            run("tar -xzf /tmp/{} -C {}{}/".format(archive_file, path, no_ext))
            run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
            run("rm -rf {}{}/web_static".format(path, no_ext))

            run("rm /tmp/{}".format(archive_file))
            run("rm -rf /data/web_static/current")
            run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))
            return True
        except Exception:
            return False
    else:
        return False
