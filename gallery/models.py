from django.db import models


class Location(models.Model):
    '''
    class to define image location properties
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        '''
        method to save location
        '''
        self.save()

    def delete_location(self):
        '''
        method to delete location
        '''
        self.delete()


class Category(models.Model):
    '''
    class to define image category properties
    '''
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        '''
        method to save category
        '''
        self.save()

    def delete_category(self):
        '''
        method to delete category
        '''
        self.delete()


class Image(models.Model):
    '''
    class to define image properties
    '''
    image = models.ImageField(upload_to='images_storage_path/')
    image_name = models.CharField(max_length=30)
    image_description = models.CharField(max_length=150)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    @classmethod
    def all_images(cls):
        '''
        method to get all images
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls, search_term):
        # no test was run for this, kindly review later
        '''
        method that searches for images by category
        '''
        images = cls.objects.filter(category__category__icontains=search_term)
        return images

    def __str__(self):
        return self.image_name
