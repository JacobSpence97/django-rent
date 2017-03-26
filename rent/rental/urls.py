from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^store', views.store, name="store"),
    url(r'^rent/(?P<item_id>[0-9]+)/$', views.rent, name="rent"),
    url(r'^returns/(?P<item_id>[0-9]+)/$', views.returns, name="returns"),
]
