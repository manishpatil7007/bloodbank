from django.shortcuts import render
from .models import Faked1
from django.http.response import HttpResponse
import faker
fake=faker.Faker()
def fview(request):
    for i in range(100):
        first_name=fake.first_name()
        last_name=fake.last_name()
        job=fake.random_element(elements=("HR","PM","Admin","TL"))
        email=fake.email()
        salary=fake.random_element(elements=(10000,20000,30000))
        city=fake.random_element(elements=("hyd","pune","chennai","nashik"))
        dob=fake.date_time()
        address=fake.address()
        data=Faked1(
            first_name=first_name,
            last_name=last_name,
            job=job,
            email=email,
            salary=salary,
            city=city,
            dob=dob,
            address=address
                    )
        data.save()
    return HttpResponse("Data inserted")
def fecthing_data(request):
    fdata=Faked1.objects.all()
    return render(request,'fakedata.html',{'fdata':fdata})







