from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskDetails
		fields = '__all__'