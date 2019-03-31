from django.shortcuts import render,redirect
from django.http import JsonResponse
from user import user_decorator
from django.db import transaction
from datetime import datetime
from decimal import Decimal
from user.models import AddressInfo
from cart.models import CartInfo
from goods.models import GoodsInfo
from .models import OrderInfo,OrderDetail

@user_decorator.login
def order(request):
    cid =request.GET.get('cid')
    cids = cid.split(',')
    price =request.GET.get('price')
    uid = request.session['user_id']
    address_list = AddressInfo.objects.filter(auser_id = uid)
    goods_list = CartInfo.objects.filter(id__in=cids)
    context={
        'title':'提交订单',
        'address_list':address_list,
        'goods_list':goods_list,
        'price':price,
        'cid':cid 
    }
    return render(request,'order/pay.html',context)

@transaction.atomic()  #类似于回滚操作
@user_decorator.login
def orderHandle(request):
    tran_id = transaction.savepoint() #建一个回退的点
    cart_id = request.POST.get('cid') #接收购物车编号
    now = datetime.now()  #需要引用模板
    uid = request.session['user_id']
    data={}
    try:
        order = OrderInfo()
        order.onumber = '%s%d'%(now.strftime('%Y%m%d%H%M%S'),uid)
        order.user_id = uid
        order.odate = now
        order.ototal = request.POST.get('price')
        order.oaddress_id=request.POST.get('address_id')
        order.opostage=0
        order.save()
        cart_ids = cart_id.split(',')
        for item in cart_ids:
            cart = CartInfo.objects.get(pk=int(item))
            goods = cart.goods
            goods.ginventory = cart.goods.ginventory-cart.count
            goods.save()
            defail = OrderDetail()
            defail.order=order
            defail.ocount = cart.count
            defail.ogoods_id = goods.id
            defail.save()
            cart.delete()
        data['ok'] = 1
        transaction.savepoint_commit(tran_id) #提交后才真正作用到服务器上    
    except Exception as e:
        print("%s" % e)
        data['ok'] = 0
        transaction.savepoint_rollback(tran_id)  # 事务任何一个环节出错，则事务全部取消
    return JsonResponse(data)
  

@user_decorator.login
def orderList(request):  #订单列表
    uid = request.session['user_id']
    order_list =  OrderInfo.objects.filter(user_id=uid)
    cart_list=[]
    for item in order_list:
        cart_id = item.ocart.split(',') #循环一笔订单多个商品的数据
        if len(cart_id)>1:   #如果只有一个商品就不需要循环
            for idx in cart_id:
                cart_list.append(CartInfo.objects.get(id=idx))
        else:
            cart_list.append(CartInfo.objects.get(id=item.ocart))
    context={
        'title':'订单列表',
        'order_list':order_list,
        'cart_list':cart_list,
    }
    return render(request,'order/order.html',context)
""" 
事务：一旦操作失败全部回退
1、创建订单对象 
2、判断商品库存 应该从购物车就开始判断
3、创建详单对象
4、修改相对应的商品库存
5、删除购物车对应的商品
"""


@user_decorator.login
def pay(request,oid):
    order = OrderInfo.objects.get(oid=oid)
    order.oIsPay = True
    order.save()
    context = {
        'order':order
    }
    return render(request,'order/pay.html',context)