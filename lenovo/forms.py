from django import forms
from .models import lenovothink


class lenovo_laptop(forms.ModelForm):
    class Meta:
        model = lenovothink
        fields = ['user', 'name', 'brand', 'harddrive','value','material']