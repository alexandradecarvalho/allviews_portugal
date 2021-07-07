from django.shortcuts import render

from app.models import Frame, Photo, Brand, BrandPhoto


# Create your views here.
# def index(request):
#   tparams = {'brands':[]}
#  existing_frames = []
#
#   for photo in Photo.objects.all():
#      if name := photo.frame.name not in existing_frames: # show only 1 photo per frame
#         existing_frames += [name]
#        if brand := photo.frame.brand not in tparams:
#           tparams[brand] = []
#      tparams[brand] += [photo] #divides existing photos by brand
#
#   for photo in BrandPhoto.objects.all():
#      tparams['brands'] += [(photo, photo.brand.name)]
#
#   return render(request, 'index.html', tparams)


def index(request):
    tparams = {'brands': []}

    considered_brands = []

    for brand_photo in BrandPhoto.objects.all():
        if brand_photo.brand.name not in considered_brands:
            considered_brands += [brand_photo.brand.name]
            frame_record = []
            for frame in Frame.objects.filter(brand=brand_photo.brand):
                frame_record += [(frame.name, Photo.objects.filter(frame=frame)[0])]

            tparams['brands'] += [((brand_photo.brand.name, brand_photo), frame_record)]

    return render(request, 'index.html', tparams)
