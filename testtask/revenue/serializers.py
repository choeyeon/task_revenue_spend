from rest_framework import serializers
from .models import *


class RevenueStatisticSerializer(serializers.ModelSerializer):
    total_revenue = serializers.DecimalField(max_digits=9, decimal_places=2)
    spend_value = serializers.DecimalField(max_digits=10, decimal_places=2)
    impressions = serializers.IntegerField()
    clicks = serializers.IntegerField()
    conversion = serializers.IntegerField()

    class Meta:
        model = RevenueStatistic
        fields = ['name', 'date', 'total_revenue', 'spend_value', 'impressions', 'clicks', 'conversion']

