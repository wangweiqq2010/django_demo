#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect


# from models import Test

def index(request):
    return render(request, 'infomanage/index.html')


def special_case_2018(request):
    context = {'msg':'2018 : special_case_2018'}
    return render(request, "infomanage/matchtest.html",context)


def year_archive(request, year):
    context = {'msg': year + ' : year_archive'}
    return render(request, "infomanage/matchtest.html", context)


def month_archive(request, year, month):
    context = {'msg': year + '.' + month + ' : month_archive'}
    return render(request, "infomanage/matchtest.html", context)


def group_year_archive(request, year):
    return render(request, "infomanage/group_year.html", locals())


def group_month_archive(request, year, month):
    return render(request, "infomanage/group_month.html", locals())


def extra_parameter(request, year, month):
    return render(request, "infomanage/group_month.html", locals())


def add_test(request):
    return render(request, "infomanage/add_test.html")


def add(request, first, second):
    add_result = int(first) + int(second)
    msg = str(first) + "+" + str(second) + "=" + str(add_result)
    return HttpResponse("<h1>" + msg + "</h>")


def old_add_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('new_add', args=(a, b))
    )

# def hello(request, name):
#     print name
#     context = {'name': name}
#     return render(request, 'hello/index.html', context)
#
# def testdb(request):
#     # response = ""
#     # list = Test.objects.all()
#     # for a in list:
#     #     response += a.name + " " + str(a.age) + '\n'
#     # print response
#     # print "*"*30
#     # response = ""
#     # list = Test.objects.filter(name='wangwei')
#     # for var in list:
#     #     response += str(var.id) + " " + var.name + '\n'
#     # print response
#     # print "*"*30
#     # test1 = Test.objects.get(id = 2)
#     # response = test1.name
#     # print response
#     # print "*"*30
#     # response = ""
#     # list = Test.objects.order_by("age")[1:]
#     # for var in list:
#     #     response += str(var.id) + " " + var.name + '\n'
#     # print response
#     # print "*"*30
#     # Test.objects.filter(name='wangwei').update(name='baidu')
#     # Test.objects.get(id=2).delete()
#     return HttpResponse("<p>数据添加成功！</p>")
#

#
# def search(request):
#     request.encoding = 'utf8'
#     if 'q' in request.GET:
#         message = "你搜索的是：" + request.GET['q']
#     else:
#         message = "你提交了空表单"
#     return HttpResponse(message)
#
# def search_post(request):
#     ctx ={}
#     if request.POST:
#         ctx['rlt'] = request.POST['q']
#     return render(request, "hello/post.html", ctx)
#
# def index1(req,id):
#     print (id)
#     print (locals())
#     return render(req,"hello/index1.html")
