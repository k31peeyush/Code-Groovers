from rest_framework import serializers
from .models import H1BData

class H1BSerializer(serializers.ModelSerializer):
    class Meta:
        model = H1BData
        fields = ('case_number', 'wage_rate_of_pay', 'wage_unit_of_pay')
