from rest_framework.serializers import ModelSerializer
from user.models import LoanRequest

class LoanRequestSerializer(ModelSerializer):
    class Meta:
        model = LoanRequest
        fildes = ['owner', 'amount', 'months']