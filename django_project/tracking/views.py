from django.contrib.sites.shortcuts import get_current_site
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.views import View

from .models import HTTPRequestInfo, TrackingGroup


class TrackingView(View):

    def get(self, request, entry_name, *args, **kwargs):

        group = get_object_or_404(TrackingGroup, entry_name=entry_name)

        meta_dict = request.META
        http_user_agent = meta_dict['HTTP_USER_AGENT']
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        http_referer = meta_dict.get('HTTP_REFERER', '')

        HTTPRequestInfo.objects.create(
            group=group,
            ip_address=ip,
            user_agent=http_user_agent,
            referer=http_referer,
        )
        redirection = group.redirect_url
        if redirection is None:
            raise Http404
        return redirect(redirection)
