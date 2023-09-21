command = '/home/debian/projects/aproo/env/bin/gunicorn'
pythonpath = '/home/debian/projects/aproo/aproo/'
bind = '127.0.0.1:8200'
workers = 5
user = 'debian'
limit_request_fields = 32000
limit_request_fields_size = 0
rav_env = 'DJANGO_SETTINGS_MODULE=aproo.settings'
