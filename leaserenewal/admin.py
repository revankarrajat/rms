from django.contrib import admin

# Register your models here.
from.models import leaserenewal,renewal

class leaserenewaladmin(admin.ModelAdmin):
    last_display = ["id","landlord_name","tenant_name","property","start_date"," end_date","balance "," security_deposit ","city"," state","pincode"]

    class Meta:
        model = leaserenewal

class renewaladmin(admin.ModelAdmin):
    last_diaplay = ["id","renewaldate","renewalperiod","lease_id"]

    class Meta:
        model = renewal


admin.site.register(leaserenewal,leaserenewaladmin)
admin.site.register(renewal,renewaladmin)

