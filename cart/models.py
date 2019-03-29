from django.db import models

class CartInfo(models.Model):
    user = models.ForeignKey('user.UserInfo',on_delete=models.CASCADE)#引用别的应用模板 应用名加模板名
    goods = models.ForeignKey('goods.GoodsInfo',on_delete=models.CASCADE)
    count = models.IntegerField()