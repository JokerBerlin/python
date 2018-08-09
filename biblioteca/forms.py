from django import forms
from . import models

class AutorForm(forms.ModelForm):
	class Meta:
		model = models.Autor
		fields = '__all__'

class EditorForm(forms.ModelForm):
	class Meta:
		model = models.Editor
		fields = '__all__'
