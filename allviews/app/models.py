from django.db import models


# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BrandPhoto(models.Model):
    picture = models.ImageField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Frame(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    sex = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Photo(models.Model):
    picture = models.ImageField()
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

