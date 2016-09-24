#!/usr/bin/env bash

docker pull postgres:9.5.4

docker run --name python-etl-postgres -e POSTGRES_PASSWORD=root -p 5432:5432 -d postgres:9.5.4
