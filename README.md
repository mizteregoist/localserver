# localserver
The simple docker container helps you to develop more awesome web apps

If you haven't python3 on your machine, install it for generating .env file.

Before run docker container you need to generate .env file by run command:
> python init_env.py

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