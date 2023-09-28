from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from django.db.models import Sum, F
from rest_framework.response import Response
from rest_framework.views import APIView


class RevenueStatisticViewSet(ModelViewSet):
    queryset = RevenueStatistic.objects.all()
    serializer_class = RevenueStatisticSerializer

    def get_queryset(self):
        return self.queryset.values('name', 'date').annotate(
            total_revenue=Sum('revenue'),
            spend_value=F('spend__spend'),
            impressions=F('spend__impressions'),
            clicks=F('spend__clicks'),
            conversion=F('spend__conversion')
        )
