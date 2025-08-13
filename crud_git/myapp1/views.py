from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    uid = Employee.objects.all()
    context = {
        'uid':uid,
    }
    return render(request, 'index.html', context)