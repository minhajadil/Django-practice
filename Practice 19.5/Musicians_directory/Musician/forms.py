from django import forms 
from .models import MusicianDB


class MusicianForm(forms.ModelForm):
    class Meta :
        model = MusicianDB
        fields='__all__'