from django import forms
from .models import AlbumDB

class AlbumForm(forms.ModelForm):
    class Meta:
        model = AlbumDB
        fields='__all__'