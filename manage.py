#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import functools
import os
import sys


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


def main():
    monkey_patch_resolver_match()

    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangoapp.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
