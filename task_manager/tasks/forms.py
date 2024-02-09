from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ClearableFileInput



class TaskForm(forms.ModelForm):
	image = models.ImageField(blank=True)
	class Meta:
		model = TaskDetails
		fields = '__all__'