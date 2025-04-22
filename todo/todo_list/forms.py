from django import forms
from .models import List  # make sure this is importing your model correctly


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ['item', 'completed']
