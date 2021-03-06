# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('dashboards.views',
    # url(r'^$', redirect_to, {'url': 'home'}),
    # url(r'^home$', 'home', name='home'),
    url(r'^mobile$', 'mobile', name='home.mobile'),
    url(r'^dashboards/revisions$', 'revisions', name='dashboards.revisions'),
    url(r'^dashboards/user_lookup$', 'user_lookup',
        name='dashboards.user_lookup'),
    url(r'^dashboards/topic_lookup$', 'topic_lookup',
        name='dashboards.topic_lookup'),
    url(r'^localization$', 'localization', name='dashboards.localization'),
    url(r'^contributors$', 'contributors', name='dashboards.contributors'),
    url(r'^wiki-rows/(?P<readout_slug>[^/]+)', 'wiki_rows',
        name='dashboards.wiki_rows'),
    url(r'^localization/(?P<readout_slug>[^/]+)', 'localization_detail',
        name='dashboards.localization_detail'),
    url(r'^contributors/(?P<readout_slug>[^/]+)', 'contributors_detail',
        name='dashboards.contributors_detail'),
)
