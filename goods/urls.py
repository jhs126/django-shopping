from django.urls import path
from goods import views
from .views import MySearchView  
# from views import *
urlpatterns = [
    path('',views.index,name='home'),
    path('goods/list/<int:tid>/<int:pindex>/<int:sort>/',views.list,name='goodslist'),
    path('goods/<int:gid>/',views.detail,name='goodsdetail'),
    path('search', MySearchView(),name='search'),
]
