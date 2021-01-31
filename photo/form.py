from django.forms import ModelForm
from photo.models import Photobook

class PhotoForm(ModelForm):
    class Meta:
        model=Photobook
        fields='__all__'



class PhotoForm2(ModelForm):
    class Meta:
        model=Photobook
        fields=['caption','image','description',]