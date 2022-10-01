from django.contrib.sitemaps import Sitemap
from .models import *
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    "Site map class for statis urls"
    def items(self):
        return ['degtorad','radtodeg','supplementary', 'complementary', 'reflex']

    def location(self, item):
        return reverse(item)


class DegreeSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=1000
    def items(self):
        return degtorad.objects.all()

    def location(self, obj):
        return obj.url

    def lastmod(self, obj): 
        return obj.date_modified

class RadianSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=1000
    def items(self):
        return radtodeg.objects.all()

    def location(self, obj):
        return obj.url

    def lastmod(self, obj): 
        return obj.date_modified

class SupplementarySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=1000
    def items(self):
        return supplementary.objects.all()

    def location(self, obj):
        return obj.url

    def lastmod(self, obj): 
        return obj.date_modified


class ComplementarySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=1000
    def items(self):
        return complementary.objects.all()

    def location(self, obj):
        return obj.url

    def lastmod(self, obj): 
        return obj.date_modified




class ReflexSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    limit=1000
    def items(self):
        return reflex.objects.all()

    def location(self, obj):
        return obj.url

    def lastmod(self, obj): 
        return obj.date_modified

    