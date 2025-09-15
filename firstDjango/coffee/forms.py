from django import forms
from .models import CoffeeVariety


class CoffeeVarietyForm(forms.Form):
   coffee_variety = forms.ModelChoiceField(queryset= CoffeeVariety.objects.all(), label="Select Coffee Variety")
   #coffee_variety = forms.CharField()