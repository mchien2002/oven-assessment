"""
ASGI config for djangoapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
import functools
import os

from django.core.asgi import get_asgi_application


def monkey_patch_resolver_match():
    import django.urls.resolvers
    OriginalResolverMatch = django.urls.resolvers.ResolverMatch

    class PatchedResolverMatch(OriginalResolverMatch):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

        @property
        def function_name(self):
            if isinstance(self.func, functools.partial):
                return repr(self.func)
            else:
                return self._func_path

    django.urls.resolvers.ResolverMatch = PatchedResolverMatch


monkey_patch_resolver_match()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapp.settings")

application = get_asgi_application()
