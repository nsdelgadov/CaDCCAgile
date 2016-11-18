from __future__ import unicode_literals

from django.apps import AppConfig


class CadccConfig(AppConfig):
    name = 'cadcc'
    verbose_name = "CaDCC"

    def ready(self):
        import cadcc.signals.handlers
