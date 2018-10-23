from django import forms
from .models import lenovothink


class lenovo_laptop(forms.ModelForm):
    class _meta:
        model = lenovothink
        fields = ['user', 'name', 'brand', 'harddrive','value','material']
