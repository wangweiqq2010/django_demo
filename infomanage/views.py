#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# from models import Test

def index(request):
    return render(request, 'infomanage/index.html')


def special_case_2018(request):
    context = {'msg':'2018 : special_case_2018'}
    return render(request, "infomanage/matchtest.html",context)


def year_archive(request, year):
    context = {'msg': year + ' : year_archive'}
    return render(request, "infomanage/matchtest.html", context)


def month_archive(request, year,month):
    context = {'msg': year + '.'+ month + ' : month_archive'}
    return render(request, "infomanage/matchtest.html", context)

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
# def search_form(request):
#     return render(request, 'hello/search_form.html')
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
