#!/usr/bin/env bash

docker pull mysql:latest

docker run --name python-etl-mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql:latest
