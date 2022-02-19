import os


FROM_EMAIL = 'calendar'
SERVER_EMAIL = f'{FROM_EMAIL} <{os.environ["SERVER_EMAIL"]}>'
EMAIL_HOST = os.environ['EMAIL_HOST']
EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']
EMAIL_PORT = int(os.environ['EMAIL_PORT'])
EMAIL_USE_TLS = bool(int(os.environ['EMAIL_USE_TLS']))
