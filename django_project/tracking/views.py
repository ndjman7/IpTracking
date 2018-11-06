from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.views import View

from .models import HTTPRequestInfo, Redirection


class TrackingView(View):

    def get(self, request, *args, **kwargs):
        meta_dict = request.META
        http_user_agent = meta_dict['HTTP_USER_AGENT']
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        http_referer = meta_dict.get('HTTP_REFERER', '')

        HTTPRequestInfo.objects.create(
            ip_address=ip,
            user_agent=http_user_agent,
            referer=http_referer,
        )
        redirection = Redirection.objects.last()
        if redirection is None:
            site = get_current_site(request)
            return redirect(str(site) + '/admin/')
        return redirect(redirection.url)
