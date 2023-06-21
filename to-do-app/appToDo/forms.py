from django import forms
from .models import *
class AddRecordForm(forms.ModelForm):
	title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"title", "class":"form-control"}), label="Title")

	class Meta:
		model = ToDoInfo
		exclude = ("user",)