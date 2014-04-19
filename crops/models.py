from django.db import models
# Create your models here.

class Crop(models.Model):
	name = models.CharField(max_length=250)
	type_crop_choices = (('Rabi',  'Rabi'), ('Kharif', 'Kharif'))
	type_crop = models.CharField(max_length=250, choices=type_crop_choices)
	location = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=5, decimal_places=3)
	owner = models.ForeignKey('users.CustomUser')
	expiry = models.DateField()

	def __unicode__(self):
		return self.name + " | " + self.owner.username

