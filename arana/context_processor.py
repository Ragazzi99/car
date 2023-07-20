from . models import *


def slick(request):
    info = AppInfo.objects.get(pk=1)

    context = {
        'info':info,
    }

    return context