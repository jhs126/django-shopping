from django.urls import path
from user import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('registerhandle/', views.registerHandle),
    path('registerisname', views.registerIsName),
    path('login/', views.login,name='login'),
    path('loginhandle/', views.loginHandle),
    path('info/', views.Info,name='info'),
    path('order/<int:pindex>', views.order,name='order'),
    path('address/', views.address,name='address'),
    path('addressdel<int:id>/', views.addressDel),
    path('addresshandle<int:id>/', views.addressHandle),
    path('addressdefault<int:id>/', views.addressDefault),
    path('logout/', views.logout,name='logout'),
    path('footmark/', views.footMark,name='footmark'),

]
