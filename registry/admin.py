from django.contrib import admin
from .models import RegionCategory, StakeholderCategory, FlightCategory, FlightPhaseCategory, SubscriptionContentType

admin.site.register(RegionCategory)
admin.site.register(StakeholderCategory)
admin.site.register(FlightCategory)
admin.site.register(FlightPhaseCategory)
admin.site.register(SubscriptionContentType)
