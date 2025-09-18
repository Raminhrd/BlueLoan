from django.urls import path
from user.views import *



urlpatterns = [
    path('add-loan-request/<str:user_id>/<int:amount>/<int:months>/', loan_request)
]