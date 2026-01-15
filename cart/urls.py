from django.urls import path
from . import views

urlpatterns = [
    path('',views.cart_home, name='cart-home'),
    path('cartlist/',views.cart_details, name='list-name'),
    path('details/<int:id>',views.cart_details,name = "details")
]