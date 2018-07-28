#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='infomanage_index'),

    # url匹配测试
    url(r'^matchtest/2018/$', views.special_case_2018, name="special_case_2018"),
    url(r'^matchtest/([0-9]{4})/$', views.year_archive, name="year_archive"),
    url(r'^matchtest/([0-9]{4})/([0-9]{2})/$', views.month_archive, name="month_archive"),

    # 命名组测试
    url(r'^group/(?P<year>\d{4})/$', views.group_year_archive, name="group_year_archive"),
    url(r'^group/(?P<year>\d{4})/(?P<month>\d{2})/$', views.group_month_archive, name="group_month_archive"),


    # url(r'^(\w+)/$', views.hello, name='hello'),
    # url(r'^testdb$', views.testdb, name='testdb'),
    # url(r'^search_form$', views.search_form, name='searchform'),
    # url(r'^search$', views.search, name='search'),
    # url(r'^search_post$', views.search_post, name='search_post'),
    # url(r'^index1/(?P<id>\d{3})/$',views.index1,name='index1'),

]