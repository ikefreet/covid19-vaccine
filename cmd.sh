#!/bin/sh

mysql -u root -h mydb -e "create database django;"
mysql -u root -h mydb -e "use mysql;" -e "create user 'django'@''%' identified by 'django';"
mysql -u root -h mydb -e "grant all privileges on django.* to django@'%';" -e "flush privileges;"
python3 manage.py makemigrations
python3 manage.py migrate
mysql -u root -h mydb -e "SET collation_connection = ‘utf8_general_ci’;"
mysql -u root -h mydb -e "ALTER DATABASE django CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -u root -h mydb -e "use django;" -e "ALTER TABLE pybo_question CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;" -e "ALTER TABLE pybo_reservation CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;"
python3 manage.py runserver 0.0.0.0:8080
