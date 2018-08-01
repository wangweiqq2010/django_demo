#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse

import models
import datetime
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect


# from models import Test

def index(request):
    return render(request, 'infomanage/index.html')


def special_case_2018(request):
    context = {'msg': '2018 : special_case_2018'}
    return render(request, "infomanage/matchtest.html", context)


def year_archive(request, year):
    context = {'msg': year + ' : year_archive'}
    return render(request, "infomanage/matchtest.html", context)


def month_archive(request, year, month):
    context = {'msg': year + '.' + month + ' : month_archive'}
    return render(request, "infomanage/matchtest.html", context)


def group_year_archive(request, year):
    # def group_year_archive(request, year='2018'):
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


def model_test(request):
    return render(request, "infomanage/model_test.html")


def add_teacher(request):
    if request.method == "GET":
        name = ""
        if request.GET['name']:
            name = request.GET['name']
        gender = ""
        if request.GET['gender']:
            gender = request.GET['gender']
        age = ""
        if request.GET['age']:
            age = request.GET['age']
        course = ""
        if request.GET['course']:
            course = request.GET['course']
        email = ""
        if request.GET['email']:
            email = request.GET['email']
        introduction = ""
        if request.GET['introduction']:
            introduction = request.GET['introduction']
        obj = models.Teacher(name=name, gender=gender, age=age, course=course, email=email, introduction=introduction)
        obj.save()
        return HttpResponse("<h1>添加成功</h>")
    return HttpResponse("<h1>添加失败</h>")


def add_student(request):
    if request.method == "GET":
        name = ""
        if request.GET['name']:
            name = request.GET['name']
        gender = ""
        if request.GET['gender']:
            gender = request.GET['gender']
        grade = ""
        if request.GET['grade']:
            grade = int(request.GET['grade'])
        s_class = ""
        if request.GET['s_class']:
            s_class = request.GET['s_class']
        math = 90
        if request.GET['math']:
            math = int(request.GET['math'])
        obj = models.Student(name=name, gender=gender, grade=grade, s_class=s_class, math=math)
        obj.save()
        return HttpResponse("<h1>添加成功</h>")
    return HttpResponse("<h1>添加失败</h>")


def add_math(request):
    if request.method == "GET":
        student = ""
        if request.GET['student']:
            student = request.GET['student']
        score = 90
        if request.GET['score']:
            score = request.GET['score']
        teacher = ""
        if request.GET['teacher']:
            teacher = request.GET['teacher']
        obj = models.Math(student=student, score=score, teacher=teacher)
        obj.save()
        return HttpResponse("<h1>添加成功</h>")
    return HttpResponse("<h1>添加失败</h>")


def search_test(request):
    # 查询所有
    student = models.Student.objects.all()
    for s in student:
        print s.name + "  " + str(s.math)
    print "-"*20
    # 获取单条数据，不存在则报错（不建议）
    models.Student.objects.get(id=1)

    # 获取指定条件的数据
    models.Student.objects.filter(name='xiaoming')
    # 将指定条件的数据更新
    models.Student.objects.filter(name='xiaoming').update(gender='M')

    models.Student.objects.filter(id__lt=3, id__gt=2)  # 获取id大于2 且 小于3的值

    models.Student.objects.filter(id__in=[1, 2, 3])  # 获取id等于1、2、3的数据

    models.Student.objects.filter(name__contains="xiao")

    models.Student.objects.filter(name__icontains="xiao")  # icontains大小写不敏感

    models.Student.objects.filter(name='seven').order_by('id')    # asc
    models.Student.objects.filter(name='seven').order_by('-id')   # desc

    # regex正则匹配，iregex 不区分大小写

    models.Student.objects.get(name__regex=r'^(An?|The) +')
    models.Student.objects.get(name__iregex=r'^(an?|the) +')

    # date
    #
    models.Teacher.objects.filter(join_date__date=datetime.date(2005, 1, 1))
    models.Teacher.objects.filter(join_date__date__gt=datetime.date(2005, 1, 1))

    # year
    #
    models.Teacher.objects.filter(join_date__year=2005)
    models.Teacher.objects.filter(join_date__year__gte=2005)

    return redirect(reverse(viewname="model_test"))

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
