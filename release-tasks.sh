# Script to run before releasing a new version, ensures that the 
# database is properly set up and that initial users are set up.

echo "run migrations"
python manage.py migrate

echo "create super user"
python manage.py shell < ./create_superuser.py

