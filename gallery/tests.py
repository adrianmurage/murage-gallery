from django.test import TestCase
from .models import Image, Location, Category


class LocationTestClass(TestCase):
    '''
    Location model test class
    '''
    def setUp(self):
        self.nairobi = Location(location='nairobi')

    def test_instance(self):
        '''
        method to test Location instance
        '''
        self.assertTrue(isinstance(self.nairobi, Location))

    def test_save_method(self):
        '''
        method to test save location to db functionality
        '''
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        '''
        method to test delete Location from db functionality
        '''
        self.nairobi.save_location()
        self.nairobi.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)


class CategoryTestClass(TestCase):
    '''
    Category model test class
    '''
    def setUp(self):
        self.cameras = Category(category='cameras')

    def test_instance(self):
        '''
        method to test Category instance
        '''
        self.assertTrue(isinstance(self.cameras, Category))

    def test_save_method(self):
        '''
        method to test save location to db functionality
        '''
        self.cameras.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_method(self):
        '''
        method to test delete Location from db functionality
        '''
        self.cameras.save_category()
        self.cameras.delete_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)


class ImageTestClass(TestCase):
    '''
    Image model test class
    '''
    def setUp(self):
        self.nairobi = Location(location='nairobi')
        self.nairobi.save_location()

        self.cameras = Category(category='cameras')
        self.cameras.save_category()

        self.vintage = Image(image='images_storage_path/sssdd.jpg',
                             image_name='vintage',
                             image_description='antique camera',
                             image_location=self.nairobi,
                             image_category=self.cameras)
        self.sauda = Image(image='images_storage_path/sssdd.jpg',
                           image_name='vintage',
                           image_description='antique camera',
                           image_location=self.nairobi,
                           image_category=self.cameras)                             

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()

    def test_get_all_images(self):
        '''
        method to test if all saved images can be called from db
        '''
        self.vintage.save()
        self.sauda.save()
        self.assertTrue(len(Image.objects.all()) == 2)
