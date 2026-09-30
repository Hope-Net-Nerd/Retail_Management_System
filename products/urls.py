from django.urls import path
from . import views 

#the name of the app
name_app = 'products'

urlpatterns = [
   
   path('product/<int:pk>/', views.product_detail, name='detail'),
   path('',views.product_list, name='list'),
]