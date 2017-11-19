#!/bin/bash

clear

echo "script begin"

echo "reset database"
pg:reset --confirm django-server-apps-dev

echo "rerun migations"
python ../manage.py migrate

echo "create superuser"
echo "from django.contrib.auth.models import User; import os; User.objects.create_superuser('shadowimmageAdmin', 'shadowimmage@gmail.com', os.environ['SUPERUSER_PASS'])" | python manage.py shell

echo "loading database tables:"

echo "loading keys..."
LOAD_KEYS="psql --set ON_ERROR_STOP=on "
echo "loading rtt..."
LOAD_RTT="psql --set ON_ERROR_STOP=on "


${LOAD_KEYS} <<SQL
\i ./keys_keytypes.sql
\i ./keys_keys.sql
\i ./keys_departments.sql
\i ./keys_affiliations.sql
\i ./keys_customers.sql
\i ./keys_loanterms.sql
\i ./keys_loanexceptions.sql
\i ./keys_records.sql
SQL

${LOAD_RTT} <<SQL
\i /.rtt_makers.sql
\i /.rtt_makemodel.sql
\i /.rtt_assets.sql
\i /.rtt_components.sql
\i /.rtt_categories.sql
\i /.rtt_states.sql
\i /.rtt_assetcompassembly.sql
\i /.rtt_tasks.sql
SQL

