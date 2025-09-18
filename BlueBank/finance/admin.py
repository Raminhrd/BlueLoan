from django.contrib import admin
from finance.models import *



class BankAdmin(admin.ModelAdmin):
    list_display = ['name', 'amount']
    search_fields = ['name']
    

admin.site.register(Bank)