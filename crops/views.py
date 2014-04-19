# Create your views here.
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, View
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect

from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin

from .forms import SellCropForm
from .models import Crop
from users.models import Transaction
from users.forms import BuyCropForm


class SellCropsView(LoginRequiredMixin, CreateView):
    model = Crop
    form_class = SellCropForm
    template_name = 'sell_crops.html'
    content_type = 'text/html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.save()
        return HttpResponse('Crop has been added to sale')


class ListCropsView(AjaxResponseMixin, JSONResponseMixin, ListView):
    template_name = 'list_crops.html'
    paginate_by = 4
    content_type = 'text/html'

    def get_queryset(self):
        import datetime
        return Crop.objects.filter(expiry__gt=datetime.date.today())
    
    def get_context_data(self, **kwargs):
        ctx = super(ListCropsView, self).get_context_data(**kwargs)
        qset = self.get_queryset()
        ctx['Crops'] = qset
        return ctx

    def get_ajax(self, *args, **kargs):
        qset = self.get_queryset()
        json_dict = list(qset.values())
        return self.render_json_response(json_dict)

 


class BuyCropsView(LoginRequiredMixin, CreateView):
    template_name = 'buy_crops.html'
    form_class = BuyCropForm
    model = Crop
    content_type = 'text/html'

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'GET':
            crop_id = request.GET['cropid']
            self.request.session['crop_id'] = crop_id
        return super(BuyCropsView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        quoted_price = form.cleaned_data['quoted_price']
        crop = Crop.objects.get(id=self.request.session['crop_id'])
        offerTo = crop.owner
        form.instance.offer_to = offerTo
        form.instance.offer_about = crop
        form.instance.offer_from = self.request.user
        form.save()
        del self.request.session['crop_id']
        return HttpResponse('Offer Is valid and is sent')


class EditCrop(LoginRequiredMixin, UpdateView):
    pass