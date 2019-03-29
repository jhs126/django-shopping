#coding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

#如果未登录则转到登录页面
def login(func):
    def login_fun(request,*args,**kwargs):
        if request.session.has_key('user_id'):#是否有用户id
            return func(request,*args,**kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')#没有就跳转到登录页面
            red.set_cookie('url',request.get_full_path())#获取请求的网址路径 设置成cookie
            return red
    return login_fun


"""
http://127.0.0.1:8000/user/address?type=20
request.path:表示当前路径==/user/address
request.get_full_path():表示完整路径==/user/address?type=20
"""