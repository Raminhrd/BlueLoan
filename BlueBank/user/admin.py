from django.contrib import admin
from user.models import *




admin.site.register(UserWallet)
admin.site.register(LoanRequest)
admin.site.register(Installment)