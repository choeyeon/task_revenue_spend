from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin


@admin.register( SpendStatistic)
class SpendStatisticAdmin(ModelAdmin):
    pass
