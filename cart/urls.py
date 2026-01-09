from django.urls import path
from . import views

urlpatterns = [
    path('cartlist/',views.cart_details, name='list-name'),
]