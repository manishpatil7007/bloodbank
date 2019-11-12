from django.shortcuts import render
from .models import FakeData
from django.http.response import HttpResponse

import faker
fake=faker.Faker()

def fakedata_view(request):
    for i in range(100):
        first_name=fake.first_name()
        last_name=fake.last_name()
        email=fake.email()
        job=fake.random_element(elements=('HR','PM','Admin','Manager'))
        salary=fake.random_element(elements=(10000,20000,30000,40000))
        city=fake.random_element(elements=('hyd','banglore','pune','mumbai'))
        state=fake.state()
        address=fake.address()
        data=FakeData(
            first_name=first_name,
            last_name=last_name,
            email=email,
            job=job,
            salary=salary,
            city=city,
            state=state,
            address=address
        )
        data.save()
    return HttpResponse('DataSaved')

def fetch_data(request):
    fdata=FakeData.objects.all()
    return render(request,'fakedata.html',{'fdata':fdata})

