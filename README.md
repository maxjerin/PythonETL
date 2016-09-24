# PythonETL
Python ETL samples

# Environment
1. homebrew: to manage macOs dependencies (like pip, mysql etc).
  1. http://brew.sh/
2. pip: to manage python dependencies.
  1. http://docs.python-guide.org/en/latest/starting/install/osx/
  2. `sudo easy_install pip`
3. docker to create containers
  1. https://docs.docker.com/docker-for-mac/
  2. install and start docker

# Pre-requisite
1. Install postgres using homebrew
  1. `brew install postgres`
2. Install psycopg2 using 
  1. `sudo pip install psycopg2`
3. Start postgres container
  1. `postgresql_container.sh`
4. Run individual python scripts
  1. `python create_db.py`
  2. `python create_table.py`
  3. `python insert_data.py`

# Guidelines for working on this Repo
1. Always work off a new branch.
2. Create pull request against "dev" branch.

# Tasks
1. Create scripts to install and start mysql in docker.
2. Create Python scripts to generate large amount of data (do not upload large data file to github).
3. Create scripts to create database and table in mysql.
4. Create Python ETL script to upload data file to mysql.
5. Script to automatically run Python ETL script.
