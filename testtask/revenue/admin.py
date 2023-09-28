from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin


@admin.register( RevenueStatistic)
class RevenueStatisticAdmin(ModelAdmin):
    pass
