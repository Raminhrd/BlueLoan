from django.http import HttpResponse , JsonResponse
from django.utils.timezone import now
from datetime import timedelta
from user.models import *
from finance.models import *
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.generics import ListAPIView
from serializers import *


def loan_request(request, user_id, amount, months):
    if months > 12:
        return HttpResponse('Max months is 12')
    if amount > 100000000:
        return HttpResponse('Max amount is 100000000')
    bank = Bank.objects.first()
    if amount > bank.amount :
        return HttpResponse('amount is to  high')
    LoanRequest.objects.create(
        owner_id = user_id,
        amount = amount,
        months = months,
        status = 'p'
    )
    return HttpResponse("The loan request submited!")


#@csrf_exempt
#def loan_request_post(request):
#   if request.method == 'POST':
#   data = json.loads(request.body )
#   user_id = data['user_id']
#   amount = data['amonut']
#   months = data['months']
#   if months > 12:
#       return HttpResponse('Max months is 12')
#   if amount > 100000000:
#       return HttpResponse('Max amount is 100000000')
#   bank = Bank.objects.first()
#   if amount > bank.amount :
#       return HttpResponse('amount is to  high')
#   LoanRequest.objects.create(
#       owner_id = user_id,
#       amount = amount,
#       months = months,
#       status = 'p'
#   )
#   return HttpResponse("The loan request submited!")
#    else :
#   return HttpResponse("Invalid request")


def change_request_status(request, loan_id, status):
    if status not in ['p', 'a', 'r']:
        return HttpResponse('Status incorrect')
    loan = LoanRequest.objects.get(id=loan_id)
    loan.status = status
    loan.save()
    if loan.status == 'a':
        for i in range(0, loan.months):
            Installment.objects.create(
                loan = loan,
                date = now() + timedelta(days=30 * i),
                amount = loan.amount/ loan.months
            )
            wallet = UserWallet.objects.get(owner=loan.owner)
            wallet.amount = wallet.amount +loan.amount
            wallet.save()

            bank = Bank.objects.first()
            bank.amount -=loan.amount
            bank.save()

            return HttpResponse('loan request  status changed to' + status)
        

def delete_loan_request(request, loan_id):
    if request.method == 'DELETE':  
        loan = LoanRequest.objects.get(id=loan_id)
    if loan.status == 'p':
        loan.delete()
        return HttpResponse('Loan deleted')
    else :
        return HttpResponse('Invalid request')
    

def loan_request_list(request):
    loan_request = LoanRequest.objects.all().values('owner', 'amount', 'months')

    return JsonResponse(list(loan_request), safe=False)


#class LoanRequestList(ListAPIView):
    #queryset = LoanRequest.objects.all()
    #serializer_class = LoanRequestSerializer