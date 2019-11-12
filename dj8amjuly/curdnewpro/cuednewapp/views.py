from django.shortcuts import render

from .models import ProductData
from .forms import InsertingData,DeletingData,UpdatingData
from django.http.response import HttpResponse

def Index_view(request):
    return render(request,'index.html')

def inserting_view(request):
    if request.method=='POST':
        iform=InsertingData(request.POST)
        if iform.is_valid():
            product_id=request.post.get('product_id')
            product_name=request.post.get('product_name')
            product_class=request.POST.get('product_class')
            product_color=request.POST.get('product_color')
            product_cost=request.POST.get('product_cost')

            data= ProductData(
                product_id=product_id,
                product_name=product_name,
                product_class=product_class,
                product_color=product_color,
                product_cost=product_cost
                )
            data.save()
            iform = InsertingData
            return render(request, 'insertingdata.html', {'iform': iform})
        else:
            return HttpResponse("User invalid data.")

    else:
        iform=InsertingData
        return render(request,'insertingdata.html',{'iform':iform})



def retrieve_view(request):
    return None


def updating_view(request):
    return None


class Deleting_view(object):
    pass