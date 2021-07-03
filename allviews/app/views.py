from django.shortcuts import render

from app.models import Frame, Photo, Brand


# Create your views here.
def index(request):
    tparams = {'frames': Frame.objects.all()}

    for photo in Photo.objects.all():
        brand = photo.frame.brand
        if brand not in tparams:
            tparams[brand] = []
        tparams[brand] += photo

    return render(request, 'index.html', tparams)
