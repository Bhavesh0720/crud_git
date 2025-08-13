from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
    uid = Employee.objects.all()
    context = {
        'uid':uid,
    }
    return render(request, 'index.html', context)

def add_data(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']

        uid = Employee(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        uid.save()
        return redirect('index')
    return render(request, 'index.html')