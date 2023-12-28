from django import forms


choices =['1980','1991','1910']
colors=[('B','Black'),('G','Green'),('R','Red')]

class PracticeForm(forms.Form):
    name = forms.CharField(label="Enter your name :")
    email = forms.EmailField(initial="phitron@gmail.com")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    Mommas_birth_date = forms.DateField(widget=forms.SelectDateWidget(years=choices),required=False)
    about_you = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    Favourite_Color =forms.ChoiceField(choices=colors)
    Second_third = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=colors)
    Agree_the_terms = forms.BooleanField()


    