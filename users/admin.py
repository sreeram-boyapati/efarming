from django.contrib import admin
from .models import Transaction, CustomUser


class TransactionAdmin(admin.ModelAdmin):
	list_display = ['offer_from', 'offer_to', 'offer_about', 'quoted_price']
	search_fields = ['offer_from', 'offer_to', 'offer_about']


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CustomUser)