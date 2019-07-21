from django.conf.urls import url

from . import views

app_name = 'saferdb'

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^query/$', views.CalsearchDemo.as_view(), name='query'),
    url(r'^advanced/$', views.AdvancedSearch.as_view(), name='advanced'),
    url(r'^help/$', views.help, name='help'),
    url(r'^about/$', views.about, name='about'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^demo/$', views.CalsearchDemo.as_view(), name='demo'),
    url(r'^california/$', views.CalsearchDemo.as_view(), name='demo'),

    # url(r'^csv/$', views.Echo.as_view(), name='csvout')
    # url(r'^query/\?page=[0-9+]$', views.listing, name='listing'),
    # url(r'^home/$', views.)
    # url(r'/(?P<page>\d+)/$', views.profile_advanced_show),
    # url(r'^search/$', views.profile_advanced_search),
]
