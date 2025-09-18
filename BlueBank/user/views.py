from django.http import HttpResponse , JsonResponse
from user.models import *


def loan_request(request, user_id, amount, months):
    LoanRequest.objects.create(
        owner_id = user_id,
        amount = amount,
        months = months,
        status = 'p'
    )
    return HttpResponse("The loan request submited!")