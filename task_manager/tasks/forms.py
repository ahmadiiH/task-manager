from django.forms import ModelForm
from django import forms 
from .models import Task
from django.forms.widgets import DateTimeInput
from django.utils import timezone



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "due_date"]
        widgets = {
            'due_date': DateTimeInput(attrs={"type": "date"})
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']  # فیلدهایی که در فرم نمایش می‌دهید
        labels = {
            'title': 'Enter Your New Title :',
            'description': 'Enter Your New Description :',
            'due_date': 'Enter Your New Date :'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mb-3'}),
            'description': forms.Textarea(attrs={'class': 'my-2'}),
            'due_date': forms.DateInput(attrs={'type': 'date' , "class" : "my-2"}),
        }
