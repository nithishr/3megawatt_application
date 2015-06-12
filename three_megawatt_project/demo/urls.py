from django.conf.urls import patterns, url
from demo import views

urlpatterns = patterns('',
        url(r'^$', views.sites, name='index'),
        url(r'^sites/$', views.sites, name='sites'),
        url(r'^sites/(?P<site_id>\d)/$', views.site_detail, name='site_detail'),
        url(r'^summary-average', views.summary_avg, name='summary-avg'),
        url(r'^summary', views.summary, name='summary'),
                       )
