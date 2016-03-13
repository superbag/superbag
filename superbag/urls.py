from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from main.views import (
    salepoint, contact, HomePageView, CreateRequest, LostBaggage,
    LostBaggageRu, HomePageViewRu
    )
from main.sitemap import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = patterns(
    '',
    # url(r'^blog/', include('blog.urls')),
    url(
        r'^$',
        HomePageView.as_view(template_name="index.html"),
        name='indexua'),
    url(
        r'^ru$',
        HomePageViewRu.as_view(template_name="ru/index.html"),
        name='indexru'),


    url(r'^lost_baggage/$', LostBaggage.as_view(), name='lost_baggage'),
    url(r'^ru/lost_baggage/$',
        LostBaggageRu.as_view(),
        name='ru_lost_baggage'),

    url(r'^create_request/$', CreateRequest.as_view(), name='create_request'),
    # url(r'^point', SalePointAPI.as_view(), name='salepoints'),
    url(r'^point', salepoint, name='salepoints'),
    url(r'^contact/?$', contact, name='contact'),

    url(r'^verytrickyadmin/', include(admin.site.urls)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'),
    (r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt')),
)
