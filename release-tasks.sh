# Script to run before releasing a new version, ensures that the 
# database is properly set up and that initial users are set up.

echo "run migrations"
python manage.py migrate

echo "create super user"
echo "echo from django.contrib.auth.models import User; import os; User.objects.create_superuser('shadowimmageAdmin', 'shadowimmage@gmail.com', os.environ['SUPERUSER_PASS'])" | python manage.py shell

