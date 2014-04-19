from django import forms
from .models import TransactionMetaInfo

class BuyCropForm(forms.Form):
	quoted_price = forms.DecimalField(max_digits=5, decimal_places=3)
	expected_delivery = forms.DateField()

class FeedBackForm(forms.ModelForm):
	class Meta:
		model = TransactionMetaInfo
		fields = ('offer_from_feedback', 'offer_to_feedback', 'comments')

