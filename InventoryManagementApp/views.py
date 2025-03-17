from django.shortcuts import render,HttpResponseRedirect
from .models import  CategoryTable, CustomerTable, SupplierTable

def Login(request):
    return render(request,('Login.html'))

def Home(request):
    return render(request,'Home.html')

def Category_list(request):
    if request.method=="POST":
        Category=request.POST['Category']
        CategoryTable.objects.create(Category=Category) 
    categoriesdata=CategoryTable.objects.all()
    return render(request,'CategoryList.html',{'categoriesdata':categoriesdata})

def update_Category(request,id):
    categorydata=CategoryTable.objects.get(id=id)
    if request.method=="POST":
        Category=request.POST['Category']
        categorydata.Category=Category
        categorydata.save()
        return HttpResponseRedirect('/Categories/')
    return render(request,'CategoryList.html',{'categorydata':categorydata})

def delete_Category(request,id):
    data= CategoryTable.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/Categories/')

def Customer_list(request):
    if request.method=="POST":  
          c_name=request.POST['c_name']
          c_address=request.POST['c_address']
          c_email=request.POST['c_email']
          c_phone=request.POST['c_phone']
          CustomerTable.objects.create(c_name=c_name,c_address=c_address,c_email=c_email,c_phone=c_phone)
    customerdata=CustomerTable.objects.all()      
    return render(request,'CustomerList.html',{'customerdata':customerdata})

def delete_Customer(request,id):
    data= CustomerTable.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/Customers/')

def Supplier_list(request):
     if request.method=="POST":  
          s_name=request.POST['s_name']
          s_address=request.POST['s_address']
          s_email=request.POST['s_email']
          s_phone=request.POST['s_phone']
          SupplierTable.objects.create(s_name=s_name,s_address=s_address,s_email=s_email,s_phone=s_phone)
     supplierdata=SupplierTable.objects.all() 
     return render(request,'SupplierList.html',{'supplierdata':supplierdata})

def delete_Supplier(request,id):
    data= SupplierTable.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/Suppliers/')

def OutgoingProduct_list(request):
    return render(request,'OutgoingProducts.html')

def PurchaseProduct_list(request):
    return render(request,'PurchaseProducts.html')


# def Product_details(request):
#     if request.method=="POST":
#         Name=request.POST['Name']
#         desc=request.POST['desc']
#         quantity=request.POST['quantity']
#         price=request.POST['price']
#         productTable.objects.create(Name=Name,desc=desc,quantity=quantity,price=price)
#     return render(request,'ProductForm.html',)

# def Product_list(request):
#     data=productTable.objects.all()
#     return render(request,'ProductList.html',{'data':data})

# def update_Product(request,id):
#     data=productTable.objects.get(id=id)
#     if request.method=="POST":
#         Name=request.POST['Name']
#         desc=request.POST['desc']
#         quantity=request.POST['quantity']
#         price=request.POST['price']
#         data.Name=Name
#         data.desc=desc
#         data.quantity=quantity
#         data.price=price
#         data.save()
#         return HttpResponseRedirect('/Products/')
#     return render(request,'updateProduct.html',{'data':data})

# def delete_Product(request,id):
#     data= productTable.objects.get(id=id)
#     data.delete()
#     return HttpResponseRedirect('/Products/')