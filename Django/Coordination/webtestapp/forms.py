from django import forms
from .models import Clothes
class ClothesAdd(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['genre','kinds','size','pattern','color','image']