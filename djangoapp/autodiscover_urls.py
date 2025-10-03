import importlib

from django.conf import settings
from django.urls import include, path


def autodiscover_urlpatterns():
    discovered_patterns = []
    for app in settings.INSTALLED_APPS:
        try:
            if app.startswith("applications."):
                print(app)
                urls_module = importlib.import_module(f"{app}.urls")
                discovered_patterns.append(
                    path(f"{app.replace('applications.', '')}/", include(urls_module))
                )
        except ModuleNotFoundError as e:
            print(f"Error in autodiscover_urlpatterns with {e}")
            pass
    return discovered_patterns
