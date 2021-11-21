from django import forms
from .models import Parent, Child

class ParentForm(forms.ModelForm):
    class Meta:
        model = Parent
        fields = ['name',]

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['parent', 'name']
