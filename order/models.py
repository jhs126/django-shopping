from django.db import models

class OrderInfo(models.Model):
    onumber = models.CharField(max_length=20) #订单编号
    user = models.ForeignKey('user.UserInfo',on_delete=models.CASCADE) 
    odate = models.DateTimeField(auto_now=True) #日期
    oIsPay = models.BooleanField(default=False) #是否支付
    ototal = models.DecimalField(max_digits=8, decimal_places=2) #总支付
    oaddress = models.ForeignKey('user.AddressInfo',on_delete=models.CASCADE) #地址Id
    opostage = models.DecimalField(max_digits=4,decimal_places=2) #邮费

class OrderDetail(models.Model):
    ogoods = models.ForeignKey('goods.GoodsInfo',on_delete=models.CASCADE)
    order = models.ForeignKey(OrderInfo,on_delete=models.CASCADE)
    ocount = models.IntegerField(default=0) #数量



