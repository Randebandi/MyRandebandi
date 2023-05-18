"""
Django settings for myrandebandi project.
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('JUNTAGRICO_SECRET_KEY')

DEBUG = os.environ.get("JUNTAGRICO_DEBUG", 'True')=='True'

ALLOWED_HOSTS = ['meine.randebandi.ch','myrandebandi.juntagrico.science', 'localhost',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'juntagrico',
    'impersonate',
    'crispy_forms',
    'myrandebandi',
    'adminsortable2',
    'polymorphic',
]

ROOT_URLCONF = 'myrandebandi.urls'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('JUNTAGRICO_DATABASE_ENGINE','django.db.backends.sqlite3'), 
        'NAME': os.environ.get('JUNTAGRICO_DATABASE_NAME','myrandebandi.db'), 
        'USER': os.environ.get('JUNTAGRICO_DATABASE_USER'), #''junatagrico', # The following settings are not used with sqlite3:
        'PASSWORD': os.environ.get('JUNTAGRICO_DATABASE_PASSWORD'), #''junatagrico',
        'HOST': os.environ.get('JUNTAGRICO_DATABASE_HOST'), #'localhost', # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': os.environ.get('JUNTAGRICO_DATABASE_PORT', False), #''', # Set to empty string for default.
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'debug' : True
        },
    },
]

WSGI_APPLICATION = 'myrandebandi.wsgi.application'


LANGUAGE_CODE = 'de'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

DATE_INPUT_FORMATS =['%d.%m.%Y',]

AUTHENTICATION_BACKENDS = (
    'juntagrico.util.auth.AuthenticateWithEmail',
    'django.contrib.auth.backends.ModelBackend'
)


MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'impersonate.middleware.ImpersonateMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware'
]

EMAIL_HOST = os.environ.get('JUNTAGRICO_EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('JUNTAGRICO_EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('JUNTAGRICO_EMAIL_PASSWORD')
EMAIL_PORT = int(os.environ.get('JUNTAGRICO_EMAIL_PORT', '25' ))
EMAIL_USE_TLS = os.environ.get('JUNTAGRICO_EMAIL_TLS', 'False')=='True'
EMAIL_USE_SSL = os.environ.get('JUNTAGRICO_EMAIL_SSL', 'False')=='True'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

WHITELIST_EMAILS = []

def whitelist_email_from_env(var_env_name):
    email = os.environ.get(var_env_name)
    if email:
        WHITELIST_EMAILS.append(email.replace('@gmail.com', '(\+\S+)?@gmail.com'))


if DEBUG is True:
    for key in os.environ.keys():
        if key.startswith("JUNTAGRICO_EMAIL_WHITELISTED"):
            whitelist_email_from_env(key)
            


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

IMPERSONATE = {
    'REDIRECT_URL': '/my/profile',
}

LOGIN_REDIRECT_URL = "/my/jobs"


"""
    Admin Settings
"""
ADMINS = [
    ('Admin', os.environ.get('JUNTAGRICO_ADMIN_EMAIL')),
    ('Juntagrico', os.environ.get('JUNTAGRICO_DS_EMAIL'))
]
MANAGERS = ADMINS

"""
    File & Storage Settings
"""
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

MEDIA_ROOT = 'media'

"""
     Crispy Settings
"""
CRISPY_TEMPLATE_PACK = 'bootstrap4'

VOCABULARY = {
    'member': 'Mitglied',
    'member_pl' : 'Mitglieder',
    'assignment' : 'Arbeitseinsatz',
    'assignment_pl' : 'Arbeitseinsätze',
    'share' : 'Anteilschein',
    'share_pl' : 'Anteilscheine',
    'subscription' : 'Abo',
    'subscription_pl' : 'Abos',
    'co_member' : 'Mitabonnent',
    'co_member_pl' : 'Mitabonnenten',
    'price' : 'Betriebsbeitrag',
    'member_type' : 'Mitglied',
    'member_type_pl' : 'Mitglieder',
    'depot' : 'Depot',
    'depot_pl' : 'Depots'
}
ORGANISATION_NAME = "Randebandi"
ORGANISATION_NAME_CONFIG = {"type" : "Gemüsebaukooperative",
    "gender" : "F"}
ORGANISATION_LONG_NAME = "Gemüsebaukooperative Randebandi"
ORGANISATION_ADDRESS = {"name":"Gemüsebaukooperative Randebandi", 
            "street" : "Schachenstrasse",
            "number" : "15a",
            "zip" : "6010",
            "city" : "Kriens",
            "extra" : ""}
ORGANISATION_PHONE =''
ORGANISATION_BANK_CONNECTION = {"PC" : "89-312727-9",
            "IBAN" : "CH15 0900 0000 8931 2727 9",
            "BIC" : "9000",
            "NAME" : "PostFinance AG",
            "ESR" : "89-312727-9"}
INFO_EMAIL = "info@randebandi.ch"
SERVER_URL = "www.randebandi.ch"
BUSINESS_REGULATIONS = "https://www.randebandi.ch/wp-content/uploads/2021/12/Randebandi-Betriebsreglement_2021.pdf"
BYLAWS = "https://www.randebandi.ch/wp-content/uploads/2023/02/Randebandi-Statuten_Feb2023.pdf"
MAIL_TEMPLATE = "mails/email.html"
STYLES = {'static': ['css/individual.css']}
FAVICON = "/static/img/favicono.ico"
FAQ_DOC = "https://www.randebandi.ch/gemueseabo/faq/"
EXTRA_SUB_INFO = ""
ACTIVITY_AREA_INFO = ""
SHARE_PRICE = "475"
ENABLE_SHARES = True
BASE_FEE = ""
CURRENCY = "CHF"
ASSIGNMENT_UNIT = "ENTITY"
PROMOTED_JOB_TYPES = []
PROMOTED_JOBS_AMOUNT = 2
DEPOT_LIST_GENERATION_DAYS = [1,2,3,4,5,6,7]	
BILLING = False
BUSINESS_YEAR_START = {"day":1, "month":1}
BUSINESS_YEAR_CANCELATION_MONTH = 9
MEMBERSHIP_END_MONTH = 12
IMAGES = {           'core': '/static/img/rande.png'}
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
EMAILS = {
    'welcome': 'randebandi_emails/willkommen_mail.txt',
    'co_welcome': 'randebandi_emails/mitabonnent_willkommen.txt',
    'co_added': 'randebandi_emails/mitabonnent_info.txt',
    's_created': 'randebandi_emails/anteilsschein_mail.txt',
}

FROM_FILTER = {'filter_expression': '.*@randebandi\.ch',
               'replacement_from': 'info@randebandi.ch'}

DEFAULT_FROM_EMAIL = 'info@randebandi.ch'
