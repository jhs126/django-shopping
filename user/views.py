#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import UserInfo,AddressInfo
from goods.models import GoodsInfo
from order.models import OrderInfo
from django.core.paginator import Paginator,Page
from . import user_decorator
from hashlib import sha1
import json


def register(request):
    return render(request,'user/register.html')

def registerHandle(request):#添加数据到数据库
    #接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    # urpwd = post.get('rpwd')
    uemail = post.get('email')
    #判断两次密码
    #if(upwd != urpwd):
    #    return redirect('/user/register')
    #密码加密
    s1 = sha1()
    s1.update(upwd.encode("utf8"))
    supwd = s1.hexdigest()
    #创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = supwd
    user.uemail = uemail
    user.save()
    return redirect('/user/login')

def registerIsName(request):#验证用户名是否存在
    uname = request.GET.get('uname')
    count = UserInfo.objects.filter(uname=uname).count()
    return JsonResponse({'count':count})

def login(request): #登录 获取cookie里面的用户名，并传入登录页面
    uname = request.COOKIES.get('uname','')
    context={'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request,'user/login.html',context)

def loginHandle(request):
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    users = UserInfo.objects.filter(uname=uname)
    if(len(users)==1):#判断用户名
        s1 = sha1() #加密密码
        s1.update(upwd.encode("utf8"))
        supwd = s1.hexdigest()
        if(supwd==users[0].upwd):#判断密码
            url = request.COOKIES.get('url','/')#获取请求的网址路径
            red = HttpResponseRedirect(url)#跳转到请求的网站
            request.session['user_id'] = users[0].id #储存用户id
            request.session['user_name'] = uname  #储存用户名
            return red
            #return HttpResponseRedirect('/user/info')  #redirect没有办法设置cookie值
            #red  = HttpResponseRedirect('/user/userinfo')
            #red.set_cookie('uname',uname)
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':uname,'upwd':upwd}
            return render(request,'user/login.html',context)    
    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':uname,'upwd':upwd}
        return render(request,'user/login.html',context)    

@user_decorator.login
def Info(request):
    context={
        'title':'个人信息',
        'act_nav':1
    }
    return render(request,'user/info.html',context)

@user_decorator.login
def order(request,pindex):
    uid = request.session['user_id']
    orders = OrderInfo.objects.filter(user_id=int(uid)).order_by('-odate')
    paginator = Paginator(orders,10)
    page = paginator.page(int(pindex)) 
    context={
        'title':'我的订单',
        'act_nav':2,
        'paginator': paginator,
        'page': page,
    }
    return render(request,'user/order.html',context)

@user_decorator.login
def address(request):
    uid = request.session['user_id']
    addrss_list = AddressInfo.objects.filter(auser_id=uid)
    context = {
        'title':'我的地址',
        'address_id':'9999',
        'addrss_list':addrss_list,
        'act_nav':4
    }
    return render(request,'user/address.html',context)

def addressHandle(request,id):  #新增或修改地址
    post = request.POST
    if id<9999:
        address = AddressInfo.objects.get(pk=int(id))
    else:
        address = AddressInfo() 
        address.auser_id = request.session['user_id']
   
    address.ufullname = post.get('uname')
    address.utel = post.get('utel')
    address.uaddress = post.get('uaddress')
    address.uzipcode = post.get('uzipcode')
    address.save()
    return HttpResponseRedirect('/user/address/')

def addressDel(request,id):  #删除地址
    try:
        address = AddressInfo.objects.get(pk=int(id))
        address.delete()
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)

def addressDefault(request,id):  #新增或修改地址
    try:
        AddressInfo.objects.filter(id__contains=id).update(is_default=1)
        AddressInfo.objects.exclude(id__contains=id).update(is_default=0)
        data={'ok':1}
    except Exception as e:
        data={'ok':0}
    return JsonResponse(data)




def logout(request):
    request.session.flush()  #清理缓存执行mysql
    return redirect('/')

def footMark(request):
    goods_ids = request.COOKIES.get('cookies_id')
    goods_ids= goods_ids.split(',') #切割成数组
    mark_goods=[]
    #GoodsInfo.objects.filter(id_in=goods_ids)  也可以这样查询 这样是按id的顺序 不是按浏览先后的顺序
    for id in goods_ids:
        mark_goods.append(GoodsInfo.objects.get(pk=int(id)))

    context = {
        'title':'用户中心',
        'goods':mark_goods,
        'act_nav':3
    }
    return render(request,'user/footmark.html',context)