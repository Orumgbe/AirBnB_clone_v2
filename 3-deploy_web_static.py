#!/usr/bin/python3
"""
Fabric script that creates a zipped archive and distributes an 
archive to the web servers
"""
from datetime import datetime
from fabric.api import env, put, run, local
from os.path import exists, isdir
env.user = "ubuntu"
env.hosts = ['100.25.188.21', '52.86.207.199']


def do_pack():
    """Generate a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None

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

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        print("false")
        return False
    return do_deploy(archive_path)
