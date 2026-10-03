from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    data = flightmodel.objects.all()
    return render(request,'home.html',{'data':data})