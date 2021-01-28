from django.shortcuts import render
from photo.models import Photobook

# Create your views here.
def index(request):
    a=Photobook.objects.all()
    return render(request,'photo/index.html',{'a':a})