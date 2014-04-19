from django import forms
from .models import TransactionMetaInfo, Transaction
from django.forms import extras 

class BuyCropForm(forms.ModelForm):
	class Meta:
		model = Transaction
		fields = ('expected_delivery', 'quoted_price')
		widgets = {
			'expected_delivery': extras.SelectDateWidget(),
		}


class FeedBackForm(forms.ModelForm):
	class Meta:
		model = TransactionMetaInfo
		fields = ('offer_from_feedback', 'offer_to_feedback', 'comments')

