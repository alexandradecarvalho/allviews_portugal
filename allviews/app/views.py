from django.shortcuts import render

from app.models import Frame, Photo, Brand, BrandPhoto


# Create your views here.
def index(request):
    tparams = {'brands':[]}

    for photo in Photo.objects.all():
        brand = photo.frame.brand
        if brand not in tparams:
            tparams[brand] = []
        tparams[brand] += photo #divides existing photos by brand


    for photo in BrandPhoto.objects.all():
        tparams['brands'] += [photo]

    return render(request, 'index.html', tparams)