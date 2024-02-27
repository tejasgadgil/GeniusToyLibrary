from django.db import models
import uuid

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=100,unique = True,)
    category_code = models.CharField(max_length=100,unique = True, primary_key = True)
    category_status = models.CharField(max_length=100, default = 'Active' )
    category_description = models.TextField(null=True)

    def __str__(self):
        return self.category_name
    
class Subcategory(models.Model):
    subcategory_name = models.CharField(max_length=100, unique = True)
    subcategory_code = models.CharField(max_length=100, unique = True, primary_key = True)
    subcategory_status = models.CharField(max_length=100, default = 'Active' )
    subcategory_description = models.TextField(null=True)

    def __str__(self):
        return self.subcategory_name

class Skill(models.Model):
    skill_name = models.CharField(max_length=100, unique = True, primary_key = True)
    skill_status = models.CharField(max_length=100, default = 'Active')
    skill_description = models.TextField(null=True)
    def __str__(self):
        return self.skill_name

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
    category_name = models.ForeignKey(Category,to_field='category_name', on_delete=models.SET_NULL, null=True)
    subcategory_name= models.ForeignKey(Subcategory,to_field='subcategory_name', on_delete=models.SET_NULL, null=True)
    skills = models.ManyToManyField(Skill)
    # photos = models.ManyToManyField(Photo)
    no_of_pieces = models.IntegerField(null=True)
    manufacturer = models.CharField(max_length=100, null=True)
    # for_disabled = models.BooleanField(default=False)
    description = models.TextField(null=True)
    id = models.CharField(max_length = 100, default = uuid.uuid4, unique = True, primary_key = True, editable = False)

    def __str__(self):
        return str(self.title)
