from django.shortcuts import render,redirect
from photo.models import Photobook
from photo.form import PhotoForm

# Create your views here.
def index(request):
    a=Photobook.objects.all()
    return render(request,'photo/index.html',{'a':a})



def load_form(request):
    form=PhotoForm
    return render(request,"photo/load_form.html",{'form':form})

def additem(request):
    form=PhotoForm(request.POST,request.FILES)
    form.save()
    return redirect('/')
