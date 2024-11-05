
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('klachten.html', views.klachten, name="klachten"),
    path('adresenroute.html', views.adresenroute, name="adresenroute"),
    path('onsteam.html', views.onsteam, name="onsteam"),
    path('openingstijden.html', views.openingstijden, name="openingstijden"),
    path('dienstapo.html', views.dienstapo, name="dienstapo"),
    path('privacy.html', views.privacy, name="privacy"),
    path('afhaalkluis.html', views.afhaalkluis, name="afhaalkluis"),
    path('inloop.html', views.inloop, name="inloop"),
    path('voorl.html', views.voorl, name="voorl"),
    path('iemandanders.html', views.iemandanders, name="iemandanders"),
]
