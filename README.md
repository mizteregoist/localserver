# localserver
The simple docker container helps you to develop more awesome web apps

localserver include these packages:
* MariaDB 10.2
* Postgres 12.7
* Nginx 1.21
* pgAdmin 4
* phpMyAdmin 5.1.1
* Redis 7.0

If you haven't python3 on your machine, install it for generating .env file.

Before run docker container you need to generate .env file by run command:
> py init_env.py

After generating .env file you can do these command to run docker container:
> docker-compose up -d --build

If you run localserver on Windows you can get errors about opening ports, if ports aren't opened you can run these command in terminal of administrator permissions:
> net stop hns
> 
> net start hns

PostgreSQL and MySQL store data in ./data/db directory.
Be sure you have these directories in localserver directory.

Logs stores at ./logs

For connect to PostgreSQL and MySQL use host:
> host.docker.internal

phpMyAdmin locates at localhost:5070

pgAdmin locates at localhost:5050