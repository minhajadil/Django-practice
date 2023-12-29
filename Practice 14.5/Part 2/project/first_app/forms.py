from django import forms
from first_app.models import PracticeModel


choices =['1980','1991','1910']
colors=[('B','Black'),('G','Green'),('R','Red')]


class PracticeForm(forms.ModelForm):
    class Meta :
        model = PracticeModel
        fields='__all__'

        widgets = {
            'Date_of_birth': forms.DateTimeInput(attrs={'type': 'date'}),
        }




    