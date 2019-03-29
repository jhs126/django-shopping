from django.shortcuts import render
from django.http import JsonResponse
from .models import TypeInfo,GoodsInfo
from cart.models import CartInfo
from django.core.paginator import Paginator,Page
from django.core import serializers
from django.views.decorators.cache import cache_page  

import os

# @cache_page(60 * 15) 
def index(request): #商品首页
    #查询个分类的最新4条、最热4条数据
    type_list = TypeInfo.objects.all()[1:]
    context={}
    goods_type = []
    for i in range(len(type_list)):
        goods=type_list[i].goodsinfo_set.order_by('-id')[0:4]
        goods_type.append(goods)
    goods_list = serializers.serialize("json",type_list )

    context={
        'goods_type':goods_type,
        'goods_list':goods_list,
        'type_list':type_list,
        'title':'首页',
        'is_home':1,
        'is_nav':1
    }
    return render(request,'goods/index.html',context)


# @cache_page(60 * 15)
def list(request,tid,pindex,sort):  #商品分类列表
    type_list = TypeInfo.objects.all()[1:] #商品分类
    type_info = TypeInfo.objects.get(pk=int(tid))
    if(tid==0): #判断是全部商品还是分类商品
        filter_goods= GoodsInfo.objects.all()
    else:
        filter_goods = GoodsInfo.objects.filter(gtype_id=int(tid))
    if sort == 1:
        goods_list = filter_goods.order_by('-id')
    elif sort == 2:
        goods_list = filter_goods.order_by('-gdiscount_price')
    elif sort == 3:
        goods_list = filter_goods.order_by('-gclick')
    paginator = Paginator(goods_list,10) #列表一页放10条
    page = paginator.page(int(pindex))  #当前页的数据 且包含一系列的属性
    context = {
        'title':type_info.ttitle,
        'page':page,
        'paginator':paginator,
        'type_info':type_info,
        'sort':sort,
        'tid':tid,
        'type_list':type_list,
        'is_home':0,
        'is_nav':1
    }

    return render(request,'goods/list.html',context)

# @cache_page(60 * 15)   
def detail(request,gid):  #商品详情
    type_list = TypeInfo.objects.all()[1:] 
    goods = GoodsInfo.objects.get(pk=int(gid))
    goods.gclick = goods.gclick+1  #点击商品加1 人气商品
    goods.save()
    news = GoodsInfo.objects.order_by('-gclick')[0:5]
    # news = goods.gtype_id.goodsinfo_set.order_by('-gclick')[0:2]
    context = {
        'title':goods.gtype_id,
        'goods':goods,
        'news':news,
        'type_list':type_list,
        'gid':gid,
        'is_nav':1
    }
    response = render(request,'goods/detail.html',context)

    #记录最近浏览，在用户中心使用
    cookies_id = request.COOKIES.get('cookies_id','')
    goods_id = '%d'%goods.id  #id是int类型的 变成字符串类型
    if cookies_id !='':  #判断是否有浏览记录，如果有则继续判断
        goods_ids = cookies_id.split(',') #拆分为列表
        if goods_ids.count(goods_id) >= 1:
            goods_ids.remove(goods_id) 
        goods_ids.insert(0,goods_id) #添加到第一个
        if len(goods_ids) > 10: #如果超过1个则删除最后一个
            del goods_ids[10]
        cookies_id=','.join(goods_ids) #拼接为字符串
    else:
        cookies_id = goods_id #如果没有浏览记录则直接加
    response.set_cookie('cookies_id',cookies_id) #写入cookies
    return response

from haystack.views import SearchView
class MySearchView(SearchView):   #自定义search视图
    def extra_context(self):
        type_list = TypeInfo.objects.all()[1:] 
        context = super(MySearchView,self).extra_context()
        context['title']='搜索'
        context['type_list']=type_list
        context['is_nav']=1
        return context