from django.contrib import admin
from .models import TypeInfo,GoodsInfo
from django.utils.safestring import mark_safe
class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id','ttitle']

class GoodsInfoAdmin(admin.ModelAdmin):
    fields = ['gtitle','gpic','image_data','goriginal_price',\
    'gdiscount_price','gsynopsis','ginventory','gpostage',\
    'gcontext','isDelete','gadvertis','gtype']
    list_per_page = 10
    list_display = ['id','image_data','gtitle','gdiscount_price','gtype']
    readonly_fields = ('image_data',)  #必须加这行 否则访问编辑页面会报错
    def image_data(self, obj):
        return mark_safe('<img src="http://127.0.0.1:8000/static/%s" width="60px" />' % obj.gpic.url)
    image_data.short_description = '主图图片'


  

admin.site.register(TypeInfo,TypeInfoAdmin)
admin.site.register(GoodsInfo,GoodsInfoAdmin)