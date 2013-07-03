# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render

from sumo.helpers import urlparams
from sumo.urlresolvers import reverse

from users.models import UserBan


class BanMiddleware(object):
    """
    Middleware implementing bans. HTTP requests from banned users will
    be logged out, and shown a message explaining that they are
    banned.
    
    """
    def process_request(self, request):
        if hasattr(request, 'user') and \
               request.user.is_authenticated():
            bans = UserBan.objects.filter(user=request.user,
                                          is_active=True)
            if not bans:
                return None
            logout(request)
            return render(request,
                          'users/user_banned.html',
                          {'bans': bans,
                           'path': request.path})
        return None
