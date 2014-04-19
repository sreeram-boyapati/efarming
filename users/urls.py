from django.conf.urls import patterns, include, url
from .views import FeedBackView 

urlpatterns=patterns('', 
	url('^feedback', FeedBackView.as_view(), name="feedback")
)