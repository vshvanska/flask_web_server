#!/bin/sh

#Wait for MySQL database to be ready
echo "Checking if the MySQL host ($MYSGL_HOST:$MYSGL_PORT) is ready..."
until nc -z -v -w30 $MYSGL_HOST $MYSGL_PORT;
do
  echo "Waiting for the DB to be ready..."
  sleep 2
done

exec gunicorn --bind 0.0.0.0:5000 app.app:app
