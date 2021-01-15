# # -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import re

from django.utils.http import urlquote

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(expr.lstrip('/')) for expr in settings.LOGIN_EXEMPT_URLS]


class LoginRequired(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            redirect_url = settings.LOGIN_URL
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                redirect_url += "?next=%s" % urlquote(request.get_full_path())
                return HttpResponseRedirect(redirect_url)
                # return HttpResponseRedirect(settings.LOGIN_URL)
        response = self.get_response(request)
        return response