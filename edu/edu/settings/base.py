import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecenter.apps.EcenterConfig',
    'django_extensions',

    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'crispy_forms',
    'tinymce',

    'blog',
    'users',
    'about',
    'contact',
    'courses',
    'research',
    'scholarship',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edu.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
            'listutil': 'courses.templatestags.listutil',

            }
        },
    },
]

WSGI_APPLICATION = 'edu.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
VENV_PATH = os.path.dirname(BASE_DIR)
STATIC_ROOT = os.path.join(VENV_PATH, 'static_root')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(VENV_PATH, 'media')

# Tinymce

TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
}


# Auth

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)
SITE_ID = 1
#AUTH_USER_MODEL = 'edu.User'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CRISPY FORMS

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Redirects
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Allauth configuration

ACCOUNT_SIGNUP_FORM_CLASS = 'users.forms.SignupForm'
# ACCOUNT_AUTHENTICATION_METHOD = "username"
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
# ACCOUNT_EMAIL_SUBJECT_PREFIX = "[EduCenter]"
# ACCOUNT_EMAIL_CONFIRMATION_COOLDOWN = 60
# ACCOUNT_FORMS={
#     "add_email": "edu.forms.allauth.MyAddEmailForm",
#     "change_password": "edu.forms.allauth.MyChangePasswordForm",
#     "disconnect": "edu.forms.allauth.MyDisconnectForm",
#     "login": "edu.forms.allauth.MyLoginForm",
#     "reset_password": "edu.forms.allauth.MyResetPasswordForm",
#     "reset_password_from_key": "edu.forms.allauth.MyResetPasswordKeyForm",
#     "set_password": "edu.forms.allauth.MySetPasswordForm",
#     "signup": "edu.forms.allauth.MySignUpForm"
# }
# ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 10
# ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 60
# ACCOUNT_LOGOUT_ON_PASSWORD_CHANGE = True
# ACCOUNT_LOGIN_ON_PASSWORD_RESET = False
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
# ACCOUNT_USERNAME_BLACKLIST =["educenter","edu","admin"]
# ACCOUNT_USERNAME_MIN_LENGTH = 6
# ACCOUNT_USERNAME_VALIDATORS =None


