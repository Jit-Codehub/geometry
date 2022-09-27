from django.urls import path, include
from .import views

urlpatterns = [
    path("degree-to-radian-calculator/", views.degtoradcalculator, name="degtorad"),
    path("angle-of-<angle>-in-radian/",views.taildegtoradcalculator, name="taildegtorad"),
    
    # path("radian-to-degree-calculator/", views.radtodegcalculator, name="radtodeg"),
    # path("supplementary-angle-calculator/",views.supplementarycalculator, name="supplementary"),
    # path("complementary-angle-calculator/",views.complementarycalculator, name="complementary"),
    # path("reflex-angle-calculator/", views.reflexcalculator, name="reflex"),
   
    # path("angle-of-<angle>-radian-in-degree/", views.radtodegcalculator, name="radtodeg"),
    # path("supplementary-angle-of-<angle>-in-<angle_type>/", views.supplementarycalculator, name="supplementary"),
    # path("complementary-angle-of-<angle>-in-<angle_type>/", views.complementarycalculator, name="complementary"),
    # path("reflex-angle-of-<angle>-in-<angle_type>/",views.reflexcalculator, name="reflex"),

    
]