from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *
from django.db.models import Sum, F
from rest_framework.response import Response
from rest_framework.views import APIView


class SpendStatisticViewSet(ModelViewSet):
    queryset = SpendStatistic.objects.all()
    serializer_class = SpendStatisticSerializer

    def get_queryset(self):
        return self.queryset.values('name', 'date').annotate(
            total_spend=Sum('spend'),
            total_impressions=Sum('impressions'),
            total_clicks=Sum('clicks'),
            total_conversion=Sum('conversion'),
            revenue_stat=F('revenuestatistic__revenue')
        )