from django.db import models
from tinymce.models import HTMLField

class TypeInfo(models.Model):
    ttitle = models.CharField(u'分类标题',max_length=20)
    isDelete = models.BooleanField(u'是否删除',default=False)
    def __str__(self):
        return self.ttitle
    
class GoodsInfo(models.Model):
    gtitle = models.CharField(u'标题',max_length=100)
    gpic = models.ImageField(u'主图',upload_to='goods/%Y/%m/%d')
    goriginal_price = models.DecimalField(u'原价',max_digits=6,decimal_places=2)
    gdiscount_price = models.DecimalField(u'优惠价',max_digits=6,decimal_places=2)
    gclick = models.IntegerField(u'人气',default=0)#不显示在编辑页
    gsynopsis = models.CharField(u'简介',max_length=200,default="")
    ginventory = models.IntegerField(u'库存',default=999)
    gpostage = models.DecimalField(u'邮费',max_digits=4,decimal_places=2,default=0)
    gcontext = HTMLField(u'详情',default="") 
    isDelete = models.BooleanField(u'是否删除',default=False)
    gadvertis = models.BooleanField(u'是否推荐',default=False)  
    gtype = models.ForeignKey(TypeInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.gtitle


