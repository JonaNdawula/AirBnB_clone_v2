#!/usr/bin/python3
"""
 A Fabric script that generates a .tgz
 archive from the contents of the web_static
 folder of your AirBnB Clone repo,
 using the function do_pack.
"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """
    This function
    archives the static files
    """
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    date_time = datetime.now()
    out_put = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second
    )
    try:
        print(f"Packing web_static to{out_put}")
        local(f"tar -cvzf {out_put} web_static")
        sz = os.stat(out_put).st_size
        print("web_static packed: {} -> {} Bytes".format(out_put, sz))
    except Exception:
        out_put = None
    return out_put
