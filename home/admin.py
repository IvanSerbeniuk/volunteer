from django.contrib import admin
from .models import Event, Donation

admin.site.enable_nav_sidebar = False

admin.site.register(Event)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'amount', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'email')