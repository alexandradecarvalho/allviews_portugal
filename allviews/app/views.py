from django.shortcuts import render

from app.models import Frame, Photo, Brand, BrandPhoto


# Create your views here.
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


def details(request, frame_name):
    frame = Frame.objects.filter(name=frame_name)
    tparams = {'frame': frame, 'photos': Photo.objects.filter(frame=frame)}
    return render(request, 'portfolio-details.html', tparams)
