"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Django 4.0+ compatibility monkey-patch
try:
    from django.utils import translation
    if not hasattr(translation, 'ugettext_lazy'):
        translation.ugettext_lazy = translation.gettext_lazy
    if not hasattr(translation, 'ugettext'):
        translation.ugettext = translation.gettext
    if not hasattr(translation, 'ungettext_lazy'):
        translation.ungettext_lazy = translation.ngettext_lazy
    if not hasattr(translation, 'ungettext'):
        translation.ungettext = translation.ngettext
except ImportError:
    pass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

application = get_wsgi_application()
