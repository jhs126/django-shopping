
from django.urls import path
from order import views

urlpatterns = [
    path('pay',views.order ),
    path('push',views.orderHandle ),
    path('orderlist/',views.orderList ),
]
