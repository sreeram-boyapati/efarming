from django import forms
from .models import Crop
from django.forms import widgets, extras

class SellCropForm(forms.ModelForm):
	class Meta:
		model=Crop
		fields = ('name', 'type_crop', 'location', 'price', 'expiry')
		widgets = {
			'expiry': extras.SelectDateWidget(),
		}	
