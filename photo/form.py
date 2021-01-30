from django.forms import ModelForm
from photo.models import Photobook

class PhotoForm(ModelForm):
    class Meta:
        model=Photobook
        fields='__all__'