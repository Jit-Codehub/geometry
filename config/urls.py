from django.contrib import admin
from django.urls import path, include # new
from articles.sitemaps import *
from django.contrib.sitemaps.views import sitemap,index


sitemaps = {
    'static':Static_Sitemap,
    'factor-sitemap': factor_Sitemap,
    'lcm-sitemap': lcm_Sitemap,
    'gcf-sitemap': gcf_Sitemap,
    'gcf-of-numbers-sitemap': gcf_more_Sitemap,
    'lcm-of-numbers-sitemap': lcm_more_Sitemap,
    'euclid-algorithm-hcf-sitemap':euclidian_more_Sitemap,
    'decimal-gcf-sitemap':gcf_deci,
    'decimal-lcm-sitemap':lcm_deci,
    'fractional-lcm-sitemap':lcm_frac,
    'fractional-gcf-sitemap':gcf_frac,
    'factor-tree-sitemap':fact_tree,
    'prime-factorisation-sitemap':prime_fact,
    'factor-images-sitemap':fact_image1,
    'common-factors-sitemap':common_factors_Sitemap,
    'lcd-of-numbers-sitemap':lcd_more_Sitemap,
    'gcd-of-numbers-sitemap':gcd_more_Sitemap,
    'average-percentage-sitemap':averagePercentage_Sitemap,
    'x-out-of-y-sitemap':xOutOfY_Sitemap,
    'percentage-decrease-sitemap':percentageDecrease_Sitemap,
    'percentage-inc-sitemap':percentageInc_Sitemap,
    'convert-fraction-to-decimal':frac_deci_db_Sitemap

}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')), # new
    path('percentage/', include('percent_off.urls')), # new
    path('geometry/', include('geometry.urls')),
    path('sitemap.xml', index, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.index'),
    path('<section>.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    
    #path('factor-sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #path('lcm-sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    #path('factors-of-<str:num1>/sitemap.xml', sitemap, {'sitemaps': sitemaps1}, name='django.contrib.sitemaps.views.sitemap'),
]