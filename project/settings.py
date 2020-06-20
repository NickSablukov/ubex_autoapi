import os

from configurations import Configuration, values

SETTINGS_PREFIX = ""


class ProjectConfiguration(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # dynamic params
    DEBUG = values.BooleanValue(default=True, environ_prefix=SETTINGS_PREFIX)
    SECRET_KEY = values.Value(default="12456", environ_prefix=SETTINGS_PREFIX)
    ALLOWED_HOSTS = values.ListValue(
        default=["127.0.0.1", "localhost"], environ_prefix=SETTINGS_PREFIX
    )
    # database
    DATABASES = values.DatabaseURLValue(
        default="postgres://postgres:postgres@127.0.0.1/ubex_authapi",
        environ_name="DATABASE_URL",
    )

    # static params
    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        # libs
        "rest_framework",
        "django_filters",
        "drf_yasg",
        # applications
        "api",
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
    ]

    ROOT_URLCONF = "project.urls"
    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    WSGI_APPLICATION = "project.wsgi.application"

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": (
                "django.contrib."
                "auth.password_validation.UserAttributeSimilarityValidator"
            ),
        },
        {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
        {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
        {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
    ]

    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    STATIC_URL = "/static/"
    REST_FRAMEWORK = {
        "DEFAULT_FILTER_BACKENDS": (
            "django_filters.rest_framework.DjangoFilterBackend",
        ),
    }