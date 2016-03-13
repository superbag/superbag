from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 1
    changefreq = 'daily'

    def items(self):
        return ['indexua', 'indexru', 'lost_baggage']

    def location(self, item):
        return reverse(item)
