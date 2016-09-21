#!/usr/bin/env bash

# Init docker mysql container
./mysql_container.sh

# Create database
python ././../python/create_db.py

