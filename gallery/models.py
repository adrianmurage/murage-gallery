from django.db import models


class Location(models.Model):
    '''
    class to define image location properties
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class Category(models.Model):
    '''
    class to define image category properties
    '''
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category


class Image(models.Model):
    '''
    class to define image properties
    '''
    image = models.ImageField(upload_to='images_storage_path/')
    image_name = models.CharField(max_lenth=30)
    image_description = models.CharField(max_lenth=150)
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name
