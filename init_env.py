#!/usr/bin/python

import string
import random
from pathlib import Path


def str_generator(size=16):
    chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(size))


def init():
    try:
        current_dir = Path(__file__).resolve().parent
        env_path = current_dir.joinpath('.env')
        pgsql_pass = str_generator()
        pgadmin_pass = str_generator()
        mysql_pass = str_generator()
        mysql_root_pass = str_generator()
        data = f"""# Init .env
PGSQL_USER=webapp
PGSQL_PASS={pgsql_pass}
PGSQL_NAME=webapp

PGADMIN_EMAIL=admin@webapp.local
PGADMIN_PASS={pgadmin_pass}

MYSQL_USER=webapp
MYSQL_PASS={mysql_pass}
MYSQL_NAME=webapp
MYSQL_ROOT_PASS={mysql_root_pass}

PMA_USER=root
PMA_PASSWORD={mysql_root_pass}
"""
        env = open(env_path, 'x')
        env.write(data)
        env.close()
    except FileExistsError as e:
        print('.env already exists, delete it if you want to create a new one')


if __name__ == '__main__':
    init()
