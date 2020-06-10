from django import forms


class PathologistForm(forms.Form):
    name = forms.CharField(label='Name', required=True, max_length=100)
    specialty = forms.CharField(label='Specialty', required=True, max_length=200)
    location = forms.CharField(label='Location', required=False, max_length=50)