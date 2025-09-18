from django.urls import path
from user.views import *



urlpatterns = [
    path('add-loan-request/<str:user_id>/<int:amount>/<int:months>/', loan_request),
    path('change-request-status/<int:loan_id>/<str:status>/', change_request_status),
    path('loan-delete/<int:loan_id>/', delete_loan_request),
]