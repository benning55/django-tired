from django.contrib import admin

# Register your models here.
from accounts.models import dayoff


class dayoffAdmin(admin.ModelAdmin):
    list_display = ['create_by', 'reason', 'date_start', 'date_end', 'approve_status']
    list_per_page = 10


admin.site.register(dayoff, dayoffAdmin)
