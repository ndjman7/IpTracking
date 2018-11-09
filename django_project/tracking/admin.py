from django.contrib import admin
from .models import HTTPRequestInfo, Redirection


class HTTPRequestInfoAdmin(admin.ModelAdmin):

    fieldsets = [
        ('정보', {'fields': [
            ('ip_address', 'user_agent', 'referer', ), ('memo', ),
        ]}),
    ]
    list_display = ('ip_address', 'user_agent', 'referer', 'memo', 'created_at', )

    search_fields = ('ip_address', 'referer')


admin.site.register(HTTPRequestInfo, HTTPRequestInfoAdmin)
admin.site.register(Redirection)