from django.contrib import admin
from .models import HTTPRequestInfo, Redirection, TrackingGroup


class HTTPRequestInfoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('정보', {'fields': [
            ('ip_address', 'user_agent', 'referer', ), ('memo', ),
        ]}),
    ]
    list_display = ('group', 'ip_address', 'user_agent', 'referer', 'memo', 'created_at', )

    search_fields = ('ip_address', 'referer', 'group__name')


admin.site.register(HTTPRequestInfo, HTTPRequestInfoAdmin)
admin.site.register(Redirection)


@admin.register(TrackingGroup)
class TrafficGroupAdmin(admin.ModelAdmin):
    pass
