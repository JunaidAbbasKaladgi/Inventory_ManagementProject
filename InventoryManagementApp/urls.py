from django.contrib import admin
from django.urls import path
from InventoryManagementApp import views

urlpatterns = [
    path('',views.Login,name="Login"),
    path('Home/',views.Home,name="Home"),
    # path('Products/', views.Product_list,name="Product_list"),
    path('Categories/', views.Category_list,name="Category_list"),
    path('Customers/', views.Customer_list,name="Customer_list"),
    path('Suppliers/', views.Supplier_list,name="Supplier_list"),
    path('OutgoingProducts/', views.OutgoingProduct_list,name="OutgoingProduct_list"),
    path('PurchaseProducts/', views.PurchaseProduct_list,name="PurchaseProduct_list"),
    path('updatecategory/<int:id>', views.update_Category,name="update_Category"),
    path('deletecategory/<int:id>', views.delete_Category,name="delete_Category"),
    path('deletecustomer/<int:id>', views.delete_Customer,name="delete_Customer"),
    path('deletesupplier/<int:id>', views.delete_Supplier,name="delete_Supplier"),
    # path('Product_details/', views.Product_details,name="Product_details"),
    # path('update/<int:id>', views.update_Product,name="update_Product"),
    # path('delete/<int:id>', views.delete_Product,name="delete_Product"),  
]