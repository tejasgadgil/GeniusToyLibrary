from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Skill)
admin.site.register(Product)


# from django.contrib import admin
# from .models import *

# # Register your models here.
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('id', 'skill_name', 'skill_status', 'skill_description')

# admin.site.register(Product)
# admin.site.register(Category)
# admin.site.register(Subcategory)
# admin.site.register(Skill, SkillAdmin)

