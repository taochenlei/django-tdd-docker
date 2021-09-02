import os
from django.conf import settings
import pytest


from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


DEFAULT_ENGINE = "django.db.backends.postgresql_psycopg2"


@pytest.fixture(scope="session")
def django_db_setup():
    settings.DATABASES["default"] = {
        "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
        # "HOST": os.environ["DB_TEST_HOST"],
        # "NAME": os.environ["DB_TEST_NAME"],
        # "PORT": os.environ["DB_TEST_PORT"],
        # "USER": os.environ["DB_TEST_USER"],
        # "PASSWORD": os.environ["DB_TEST_PASSWORD"],

        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "NAME": os.environ.get("SQL_DATABASE", os.path.join(BASE_DIR, "db.sqlite3")),
        "PORT": os.environ.get("SQL_PORT", "5432"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),

    }


@pytest.fixture(scope="module")
def foo():
    # set up code
    yield "bar"
    # tear down code