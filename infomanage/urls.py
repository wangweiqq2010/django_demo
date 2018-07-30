#!/usr/local/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import url,include
from . import views

# 二级路由测试
# extra_patterns = [
#     url(r'^(?P<year>\d{4})/$', views.group_year_archive, name="group_year_archive"),
#     url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', views.group_month_archive, name="group_month_archive"),
# ]

urlpatterns = [
    url('^$', views.index, name='infomanage_index'),

    # url匹配测试
    url(r'^matchtest/2018/$', views.special_case_2018, name="special_case_2018"),
    url(r'^matchtest/([0-9]{4})/$', views.year_archive, name="year_archive"),
    url(r'^matchtest/([0-9]{4})/([0-9]{2})/$', views.month_archive, name="month_archive"),

    # 命名组测试
    url(r'^group/(?P<year>\d{4})/$', views.group_year_archive, name="group_year_archive"),
    url(r'^group/(?P<year>\d{4})/(?P<month>\d{2})/$', views.group_month_archive, name="group_month_archive"),

    # 指定view的默认配置
    # url(r'group/$', views.group_year_archive, name="group_year_archive_null"),

    # 二级路由测试
    # url(r'^group/', include(extra_patterns)),

    # 额外参数测试
    url(r'^extra_parameter/(?P<year>\d{4})/$', views.extra_parameter, {"month": "06"}, name="extra_parameter"),

    # 别名测试
    url(r'^add_test/$', views.add_test, name="add_test"),
    url(r'^add/(?P<first>\d+)/(?P<second>\d+)/$', views.add, name='add'),
    # url(r'^new_add/(?P<first>\d+)/(?P<second>\d+)/$', views.add, name='new_add'),
    url(r'^my_new_add/(?P<first>\d+)/(?P<second>\d+)/$', views.add, name='new_add'),
    # 原有url仍可用
    url(r'^new_add/(\d+)/(\d+)/$', views.old_add_redirect),

    # url(r'^(\w+)/$', views.hello, name='hello'),
    # url(r'^testdb$', views.testdb, name='testdb'),
    # url(r'^search_form$', views.search_form, name='searchform'),
    # url(r'^search$', views.search, name='search'),
    # url(r'^search_post$', views.search_post, name='search_post'),
    # url(r'^index1/(?P<id>\d{3})/$',views.index1,name='index1'),

]

