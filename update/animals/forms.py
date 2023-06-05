from django import forms
from .models import Animals

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = ['species', 'sex', 'age', 'photo']