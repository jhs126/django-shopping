from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import CartInfo
from user import user_decorator

@user_decorator.login
def cart(request): #购物车
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid)
    context = {
        'title':'购物车',
        'carts':carts,
        'is_nav':0
    }
    print(carts)
    return render(request,'cart/cart.html',context)

@user_decorator.login
def addCart(request,gid,count):  #添加商品到购物车
    try:
        uid = request.session['user_id']
    #查询购物车是否有此商品，有数量增加，没有增加商品
        carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
        if len(carts)>=1:
            cart = carts[0]
            cart.count = cart.count + count
        else:
            cart = CartInfo() #新建一个新类
            cart.user_id = uid
            cart.goods_id = gid
            cart.count = count
        cart.save()
        count = CartInfo.objects.filter(user_id=uid).count()
        data={
            'ok':1,
            'count':count
        }
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)
    #如果是ajax请求 则返回json，否则转向购物车
    #if request.is_ajax():
     #   count = CartInfo.objects.filter(user_id=uid).count()
      #  return JsonResponse({'count':count})
    #else:
     #   return redirect('cart/')



@user_decorator.login
def edit(request,cart_id,count):  #编辑购物车
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        count1 = cart.count=count
        cart.save()
        data={'ok':0}
    except Exception as e:
        data={'ok':count1}
    return JsonResponse(data)

@user_decorator.login
def delete(request,cart_id):
    try:
        cart = CartInfo.objects.get(pk=int(cart_id))
        cart.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)
