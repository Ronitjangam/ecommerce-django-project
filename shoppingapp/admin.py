from django.contrib import admin
from .models import Cataegory,Product,MyImage


# Register your models here.
class CataegoryAdmin(admin.ModelAdmin):
    list_display=['id','cname']


class ProductAdmin(admin.ModelAdmin):
    list_display=['pname','price','description','pimage']

class ImageAdmin(admin.ModelAdmin):
    list_display=['name','description','img']

admin.site.register(Cataegory)
admin.site.register(Product)
admin.site.register(MyImage,ImageAdmin)
