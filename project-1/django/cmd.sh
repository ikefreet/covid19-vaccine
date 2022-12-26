#!/bin/sh

mysql -u root -pdkagh1. -h mydb -e "create databases django;"
python3 manage.py makemigrations
python3 manage.py migrate
mysql -u root -pdkagh1. -h mydb -e "SET collation_connection = ‘utf8_general_ci’;"
mysql -u root -pdkagh1. -h mydb -e "ALTER DATABASE django CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -u root -pdkagh1. -h mydb -e "use django;" -e "ALTER TABLE pybo_question CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;" -e "ALTER TABLE pybo_reservation CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;"
python3 manage.py runserver 0.0.0.0:8080
