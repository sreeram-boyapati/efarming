# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, View
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin

from .forms import FeedBackForm
from .models import TransactionMetaInfo, Transaction


class FeedBackView(LoginRequiredMixin, CreateView):
	model = TransactionMetaInfo
	form_class = FeedBackForm
	template_name = 'feedback.html'

	def dispatch(self, request, *args, **kwargs):
		if request.method == 'GET':
		    trasaction_id = request.GET['transaction_id']
    		transaction = Transaction.objects.get(id=transaction_id)
    		offer_from = transaction['offer_from']
    		offer_to = transaction['offer_to']
    		self.request.session['offer_from'] =  offer_from.id
    		self.request.session['offer_to'] = offer_to.id
    		return super(FeedBackView, self).dispatch(request, *args, **kwargs)
    		

	def form_valid(self, form):
		form.instance.offer_to = CustomUser.objects.get(id=self.request.session['offer_from'])
		form.instance.offer_from = CustomUser.objects.get(id=self.request.session['offer_to'])
		form.save()
		del self.request.session['offer_from']
		del self.request.session['offer_to']
		return HttpResponse('Feedback has been Taken')


