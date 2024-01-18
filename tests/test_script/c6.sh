#!/bin/bash
rm city_id.txt
echo ""
echo "DROP DATABSE IF EXISTS hbnb_dev_db;" | sudo mysql

echo ""

cat ./../../setup_mysql_dev.sql | sudo mysql

echo "create state and get id"
state_op = $(echo 'create State name="California"' | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HNB_TYPE_STORAGE=db ./../../console.py)
state_id=$(echo "$state_op" | grep -o -E '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-f]{12}')
echo "State ID: $state_id"
echo """

echo 'all State' | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py

echo ""

echo 'SELECT * FROM states\G' | sudo mysql -uhbnb_dev -phbnb_dev_pwdpwd hbnb_dev_db

echo ""
echo ""
city_op=$(echo "create City state_id=\"$state_id\" name=\"San_Francisco\"" | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py)
city_id=$(echo "$city_op" | grep -o -E '[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-f]{12}'
echo "City ID: $city_id"

echo 'all City' | sudo -E HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./../../console.py

echo ""

echo "$city_id" > city_id.txt
while [ ! -e city_id.txt ]; do
  sleep 1
done

echo""
