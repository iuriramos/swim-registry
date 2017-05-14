from django.contrib import admin
from .models import RegionCategory, StakeholderCategory, DataCategory, FlightPhaseCategory, SubscriptionContentType, ActivityCategory

admin.site.register(RegionCategory)
admin.site.register(StakeholderCategory)
admin.site.register(DataCategory)
admin.site.register(ActivityCategory)
admin.site.register(FlightPhaseCategory)
admin.site.register(SubscriptionContentType)
