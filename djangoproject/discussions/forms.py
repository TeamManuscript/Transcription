from django import forms
from.import models

class CreateDiscussion(forms.ModelForm):
    class Meta:
        model = models.Discussion
        fields = ['title', 'body', 'slug', 'thumb']
