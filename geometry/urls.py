from django.urls import path, include
from .import views

urlpatterns = [
    path("degree-to-radian-calculator/", views.degtoradcalculator, name="degtorad"),
    path("angle-of-<angle>-in-radian/",views.taildegtoradcalculator),


    path("radian-to-degree-calculator/", views.radtodegcalculator, name="radtodeg"),
    path("angle-of-<angle>-radian-in-degree/", views.tailradtodegcalculator),


    path("supplementary-angle-calculator/",views.supplementarycalculator, name="supplementary"),
    path("supplementary-angle-of-<angle>-in-<angle_type>/", views.tailsupplementarycalculator),


    path("complementary-angle-calculator/",views.complementarycalculator, name="complementary"),
    path("complementary-angle-of-<angle>-in-<angle_type>/", views.tailcomplementarycalculator),
    

    path("reflex-angle-calculator/", views.reflexcalculator, name="reflex"),
    path("reflex-angle-of-<angle>-in-<angle_type>/",views.tailreflexcalculator),

    
]