import os


if os.environ.get('ENV_SETTINGS_MODE') == 'devel':
    ENV_MODE = 'devel'
else:
    ENV_MODE = 'local'


if ENV_MODE == 'devel':
    from piro_docker.settings.devel import *
elif ENV_MODE == 'local':
    from piro_docker.settings.local import *