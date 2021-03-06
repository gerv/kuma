# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponsePermanentRedirect

from nose.tools import eq_
from test_utils import RequestFactory

from sumo.tests import TestCase
from sumo.urlresolvers import reverse
from sumo.views import redirect_to


class RedirectToTestcase(TestCase):
    rf = RequestFactory()

    def test_redirect_to(self):
        resp = redirect_to(self.rf.get('/'), url='home', permanent=False)
        assert isinstance(resp, HttpResponseRedirect)
        eq_(reverse('home'), resp['location'])

    def test_redirect_permanent(self):
        resp = redirect_to(self.rf.get('/'), url='home')
        assert isinstance(resp, HttpResponsePermanentRedirect)
        eq_(reverse('home'), resp['location'])

    def test_redirect_kwargs(self):
        resp = redirect_to(self.rf.get('/'), url='users.confirm_email',
                           activation_key='1234')
        eq_(reverse('users.confirm_email', args=['1234']),
            resp['location'])



class RobotsTestCase(TestCase):
    # Use the hard-coded URL because it's well-known.
    old_setting = settings.ENGAGE_ROBOTS

    def tearDown(self):
        settings.ENGAGE_ROBOTS = self.old_setting

    def test_disengaged(self):
        settings.ENGAGE_ROBOTS = False
        response = self.client.get('/robots.txt')
        eq_('Disallow: /', response.content)
        eq_('text/plain', response['content-type'])

    def test_engaged(self):
        settings.ENGAGE_ROBOTS = True
        response = self.client.get('/robots.txt')
        eq_('text/plain', response['content-type'])
        assert len(response.content) > 11
