from django import forms

from .models import Male

class MaleForm(forms.ModelForm):
    class Meta:
        model = Male
        fields = [
           "image"
        ]