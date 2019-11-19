import os
from django.core.management import execute_from_command_line
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OAuth2DjangoSampleApp.settings")
cmd = ('manage.py runserver 0.0.0.0:8000')
execute_from_command_line(cmd.split())
