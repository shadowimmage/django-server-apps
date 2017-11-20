from django.contrib.auth.models import User
import os
if User.objects.filter(email='shadowimmage@gmail.com').count() == 0:
    User.objects.create_superuser('shadowimmageAdmin', 'shadowimmage@gmail.com', os.environ['SUPERUSER_PASS'])
else:
    pass