from django.shortcuts import render

def empview(request):
    return render(request,'empdata.html')