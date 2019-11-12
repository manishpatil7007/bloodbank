from django.shortcuts import render

from curdapp2.models import ProductData
from curdapp2.forms import Inserting_data,Updating_data,Deleting_data
from django.http.response import HttpResponse
# Create your views here.

def index_view(request):
    return render(request,'index.html')



def inserting_view(request):
    if request.method=="POST":
        iform=Inserting_data(request.POST)
        if iform.is_valid():
            product_id=request.POST.get('product_id')
            product_name=request.POST.get('product_name')
            product_class=request.POST.get('product_class')
            product_color=request.POST.get('product_color')
            product_cost=request.POST.get('product_cost')

            data=ProductData(
                product_id=product_id,
                product_name=product_name,
                product_class=product_class,
                product_color=product_color,
                product_cost=product_cost
            )
            data.save()
            iform=Inserting_data()
            return render(request,'inserting_data.html',{'iform':iform})
        else:
            return HttpResponse("User Invalid data")
    else:
        iform=Inserting_data()
        return render(request,'inserting_data.html',{'iform':iform})



def retrieve_view(request):
    products=ProductData.objects.all()
    return render(request,'retrieving_data.html',{'products':products})




def updating_view(request):
    if request.method=="POST":
        uform=Updating_data(request.POST)
        if uform.is_valid():
            product_id1=request.POST.get('product_id')
            product_cost1=request.POST.get('product_cost')

            pdata=ProductData.objects.filter(product_id=product_id1)

            if pdata:
                pdata.update(product_cost=product_cost1)
                uform=Updating_data()
                return render(request,'updating_data.html',{'uform':uform})
            else:
                return HttpResponse("Invalid Product ID")
        else:
            return HttpResponse("user invalid data")
    else:
        uform=Updating_data()
        return render(request,'updating_data.html',{'uform':uform})



def deleting_view(request):
    if request.method=="POST":
        dform=Deleting_data(request.POST)
        if dform.is_valid():
            product_id1=request.POST.get('product_id')

            pdata=ProductData.objects.filter(product_id=product_id1)

            if pdata:
                pdata.delete()
                dform = Deleting_data()
                return render(request, 'deleting_data.html', {'dform': dform})
            else:
                return HttpResponse("Invalid User ID")
        else:
            return HttpResponse("User Invalid Data")
    else:
        dform=Deleting_data()
        return render(request,'deleting_data.html',{'dform':dform})