from rest_framework import serializers
from .models import *
from revenue.models import *


class SpendStatisticSerializer(serializers.ModelSerializer):
    total_spend = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_impressions = serializers.IntegerField()
    total_clicks = serializers.IntegerField()
    total_conversion = serializers.IntegerField()
    revenue_stat = serializers.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        model = SpendStatistic
        fields = ['name', 'date', 'total_spend', 'total_impressions', 'total_clicks', 'total_conversion', 'revenue_stat']