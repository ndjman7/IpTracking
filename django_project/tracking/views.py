from datetime import timedelta

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.utils import timezone
from django.views import View

from .models import HTTPRequestInfo, Redirection


class TrackingView(View):

    def get(self, request, *args, **kwargs):
        meta_dict = request.META
        http_user_agent = meta_dict['HTTP_USER_AGENT']
        remote_address = meta_dict['REMOTE_ADDR']
        http_referer = meta_dict.get('HTTP_REFERER', '')

        one_hour_ago = timezone.now() - timedelta(hours=1)
        try:
            info = HTTPRequestInfo.objects.get(
                ip_address=remote_address,
                user_agent=http_user_agent,
                created_at__gte=one_hour_ago
            )
            info.increase_visits()
        except HTTPRequestInfo.DoesNotExist:
            HTTPRequestInfo.objects.create(
                ip_address=remote_address,
                user_agent=http_user_agent,
                referer=http_referer,
            )
        redirection = Redirection.objects.last()
        if redirection is None:
            site = get_current_site(request)
            return redirect(site + '/admin/')
        return redirect(redirection.url)
