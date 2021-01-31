from django.shortcuts import render,redirect
from photo.models import Photobook
from photo.form import PhotoForm,PhotoForm2

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



# for editing


def editPhoto(request,id):
    photo=Photobook.objects.get(id=id)
    return render(request,'photo/editPhoto.html',{'photo':photo})

def updatePhoto(request, id):

    photo = Photobook.objects.get(id=id)
    form=PhotoForm2(request.POST,request.FILES, instance=photo)
    form.save()
    return redirect('/')

# for deleting
def deletePhoto(request,id):
    photo = Photobook.objects.get(id=id)
    photo.delete()
    return redirect('/')

