from django.contrib import admin
from .models import Category, Product
from mptt.admin import MPTTModelAdmin


# Register your models here.


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    # specify pixel amount for this ModelAdmin only:
    mptt_level_indent = 20


admin.site.register(Category, CategoryMPTTModelAdmin)
admin.site.register(Product)
