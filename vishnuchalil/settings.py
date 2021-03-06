import os
import dj_database_url
import dotenv

# import django.core.mail.backends.smtp.EmailBackend

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "hy79yrgha48#6s+l(=h)v1*easa)d902t1fa(o8dtsaibcl9s^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["sharecontent.herokuapp.com", "127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    "blog",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "social_django",
    "analytical",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "vishnuchalil.urls"

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
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ]
        },
    }
]

WSGI_APPLICATION = "vishnuchalil.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)

# This should already be in your settings.py

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


AUTHENTICATION_BACKENDS = (
    "social_core.backends.open_id.OpenIdAuth",  # for Google authentication
    "social_core.backends.google.GoogleOpenId",  # for Google authentication
    "social_core.backends.google.GoogleOAuth2",  # for Google authentication
    "social_core.backends.github.GithubOAuth2",  # for Github authentication
    "social_core.backends.facebook.FacebookOAuth2",  # for Facebook authentication
    "django.contrib.auth.backends.ModelBackend",
)
# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "vishnuchalil877@gmail.com"
EMAIL_HOST_PASSWORD = "M@d080797"

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/blog/"

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "272636767783-ehoadg64ma6jsn6nlpgf35ub0bpcue72.apps.googleusercontent.com"
)  # CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "JyFQcVUPvrkd65GrEYB28Wkl"  # Secret Key


AUTH_USER_EMAIL_UNIQUE = True


GOOGLE_ANALYTICS_PROPERTY_ID = "UA-145401917-1"
ANALYTICAL_AUTO_IDENTIFY = False
ANALYTICAL_INTERNAL_IPS = ["192.168.1.45", "192.168.1.57"]

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "vishnuchalil/content")

