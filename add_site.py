#!/usr/bin/python

import sys
import getopt
import platform
from pathlib import Path


def init():
    try:
        site = None
        port = None
        opts, args = getopt.getopt(sys.argv[1:], "s:p:x", ["site=", "port="])
        for opt, arg in opts:
            if opt in ("-s", "--site"):
                site = arg
            elif opt in ("-p", "--port"):
                port = arg
        if site is None:
            site = input("Enter the site name: ")
        if port is None:
            port = input("Site port: ")
        current_dir = Path(__file__).resolve().parent
        conf_path = current_dir.joinpath(f"config/etc/nginx/conf.d/{site}.conf")
        data = f"""server {{
    listen 80;
    server_name {site};

    access_log  off;
    error_log off;

    location / {{
        proxy_pass http://host.docker.internal:{port};
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }}
}}
"""
        conf = open(conf_path, 'x')
        conf.write(data)
        conf.close()

        os = platform.system()
        hosts_path = ''
        if os == 'Windows':
            hosts_path = 'C:/Windows/System32/drivers/etc/hosts'
        elif os == 'Linux':
            hosts_path = '/etc/hosts'
        if hosts_path is not None:
            hosts = open(hosts_path, 'a')
            hosts.write(f"127.0.0.1    {site}\r\n")
            hosts.close()
    except FileExistsError as e:
        print('config already exists, delete it if you want to create a new one')
    except getopt.GetoptError:
        print('add_site.py -s <site_name> -p <port>')
        print('add_site.py --site=<site_name> --port=<port>')
        sys.exit(2)
    except KeyboardInterrupt as e:
        pass


if __name__ == '__main__':
    init()
