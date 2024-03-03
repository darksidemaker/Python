from django import forms
from .models import TodoItem

class Todofroms(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title']
