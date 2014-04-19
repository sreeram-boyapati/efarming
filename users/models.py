from django.db import models
from django.contrib.auth.models import AbstractUser

from crops.models import Crop


# Create your models here.

class CustomUser(AbstractUser):
	occupation_choices = (('Farmer', 'Farmer'), ('Merchant', 'Merchant'))
	primary_occupation = models.CharField(max_length=50, choices=occupation_choices, null=True, blank=True)
	payment_id = models.CharField(max_length=50, null=True, blank=True)
	reputation = models.IntegerField(default=0)

	def __unicode__(self):
		return self.username

class Transaction(models.Model):
	offer_from = models.ForeignKey(CustomUser, related_name='offer_from')
	offer_to = models.ForeignKey(CustomUser, related_name='offer_to')
	offer_about = models.ForeignKey(Crop)
	quoted_price = models.DecimalField(max_digits=5, decimal_places=2)
	status_choices = (('Waiting', 'Waiting'), ('Failed','Failed'), ('Success', 'Success'))
	status = models.CharField(max_length=50, choices=status_choices, default='Waiting')

class TransactionMetaInfo(models.Model):
	transaction = models.OneToOneField(Transaction)
	rating_choices = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
	offer_from_feedback = models.IntegerField(choices=rating_choices)
	offer_to_feedback = models.IntegerField(choices=rating_choices)
	comments = models.CharField(max_length=250)