from django.shortcuts import render,HttpResponseRedirect
from .models import productTable

def Product_details(request):
    if request.method=="POST":
        Name=request.POST['Name']
        desc=request.POST['desc']
        quantity=request.POST['quantity']
        price=request.POST['price']
        productTable.objects.create(Name=Name,desc=desc,quantity=quantity,price=price)
    return render(request,'Home.html',)

def Products(request):
    data=productTable.objects.all()
    return render(request,'Products.html',{'data':data})

def update_Product(request,id):
    data=productTable.objects.get(id=id)
    if request.method=="POST":
        Name=request.POST['Name']
        desc=request.POST['desc']
        quantity=request.POST['quantity']
        price=request.POST['price']
        data.Name=Name
        data.desc=desc
        data.quantity=quantity
        data.price=price
        data.save()
        return HttpResponseRedirect('/Products/')
    return render(request,'updateProduct.html',{'data':data})

def delete_Product(request,id):
    data= productTable.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect('/Products/')