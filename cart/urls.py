from django.urls import path
from cart import views

urlpatterns = [
    path('',views.cart,name='cart'),
    path('add/<int:gid>/<int:count>/',views.addCart),
    path('edit<int:cart_id>_<int:count>/',views.edit),
    path('delete<int:cart_id>/',views.delete),
]
