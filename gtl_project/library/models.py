from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Subcategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Photo(models.Model):
#     image = models.ImageField(upload_to='product_photos')

#     def __str__(self):
#         return str(self.image)

class Product(models.Model):
    prod_type = models.CharField(max_length=10)
    prod_code = models.CharField(max_length=100, null=True)
    prod_name = models.CharField(max_length=500)
    #img = models.URLField(max_length=1000)
    age_from = models.IntegerField(default=0)
    age_to = models.IntegerField(default=0)
    categories = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    subcategories= models.ForeignKey(Subcategory, on_delete=models.SET_NULL, null=True)
    skills = models.ManyToManyField(Skill)
    # photos = models.ManyToManyField(Photo)
    no_of_pieces = models.IntegerField(null=True)
    manufacturer = models.CharField(max_length=100, null=True)
    for_disabled = models.BooleanField(default=False)
    description = models.TextField(null=True)
    id = models.CharField(max_length = 100, default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return str(self.title)
