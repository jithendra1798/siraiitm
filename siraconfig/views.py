from django.shortcuts import render
from siraconfig.models import Defaults

# Create your views here.
def favicon_path():
    try:
        favicon = '/media/images/default/favicon.png'
    except:
        try:
            favicon = Defaults.objects.all()[0].favicon.url
        except:
            favicon = '/static/images/default/favicon.ico'
    return favicon