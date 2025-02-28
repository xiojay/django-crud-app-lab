from django import forms
from .models import Car, Modification, Tag

class CarForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Car
        fields = ['make', 'model', 'year', 'tags'] 
        
class ModificationForm(forms.ModelForm):
    class Meta:
        model = Modification
        fields = ['name']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']