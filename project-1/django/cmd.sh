#!/bin/sh

mysql -u root -pdkagh1. -h mydb.default.svc.local
python3 manage.py makemigrations
python3 manage.py migrate
mysql -u root -pdkagh1. -e "SET collation_connection = ‘utf8_general_ci’;"
mysql -u root -pdkagh1. -e "ALTER DATABASE django CHARACTER SET utf8 COLLATE utf8_general_ci;"
mysql -u root -pdkagh1. -e "SET collation_connection = ‘utf8_general_ci’;"
mysql -u root -pdkagh1. -e "SET collation_connection = ‘utf8_general_ci’;"

use django;
ALTER TABLE pybo_reservation CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE pybo_question CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
python3 manage.py runserver 0.0.0.0:8080
