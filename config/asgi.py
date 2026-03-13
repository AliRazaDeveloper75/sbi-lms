import os
import django
# Django 4.0+ compatibility monkey-patch
try:
    from django.utils import translation, encoding
    if not hasattr(translation, 'ugettext_lazy'):
        translation.ugettext_lazy = translation.gettext_lazy
    if not hasattr(translation, 'ugettext'):
        translation.ugettext = translation.gettext
    if not hasattr(translation, 'ungettext_lazy'):
        translation.ungettext_lazy = translation.ngettext_lazy
    if not hasattr(translation, 'ungettext'):
        translation.ungettext = translation.ngettext
    if not hasattr(encoding, 'smart_text'):
        encoding.smart_text = encoding.smart_str
    if not hasattr(encoding, 'force_text'):
        encoding.force_text = encoding.force_str
except ImportError:
    pass

from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

application = ProtocolTypeRouter(
    {
        "http": AsgiHandler(),
        # Just HTTP for now. (We can add other protocols later.)
    }
)
