# boot_django.py
#
# This file sets up and configures Django. It's used by scripts that need to
# execute as if running in a Django server.
import os
import django
from django.conf import settings

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "admin_sso"))


def boot_django():
    settings.configure(
        BASE_DIR=BASE_DIR,
        DEBUG=True,
        INSTALLED_APPS=(
            "admin_sso",
        ),
    )
    django.setup()