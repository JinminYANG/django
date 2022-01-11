'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication'
),

# Authentication
'UNAUTHENTICATED_USER': 'django.contrib.auth.models.AnonymousUser',
'UNAUTHENTICATED_TOKEN': None,