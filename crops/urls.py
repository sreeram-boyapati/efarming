from django.conf.urls import patterns, include, url
from .views import BuyCropsView, SellCropsView, ListCropsView

urlpatterns=patterns('', 
	url(r'^buyCrops', BuyCropsView.as_view(), name='buyCrops'),
	url(r'^sellCrops', SellCropsView.as_view(), name='sellCrops'),
	url(r'^listcrops', ListCropsView.as_view(), name='ListCrops'),
)