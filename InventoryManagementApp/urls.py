from django.contrib import admin
from django.urls import path
from InventoryManagementApp import views

urlpatterns = [
    path('', views.Product_details,name="Product_details"),
    path('Products/', views.Products,name="Products"),
     path('update/<int:id>', views.update_Product,name="update_Product"),
    path('delete/<int:id>', views.delete_Product,name="delete_Product"),  
]