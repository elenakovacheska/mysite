from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

class NumberForm(forms.Form):
	input_number = forms.IntegerField(label='Enter a number', validators=[MaxValueValidator(10000000), MinValueValidator(2)])