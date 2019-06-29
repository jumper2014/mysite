#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from zyt import views
from django.conf.urls import url
from django.urls import path
# from . import views

app_name = 'zyt'
urlpatterns = [
    url(r'^$', views.index),
    # ex: /zyt/
    # path('', views.index, name='index'),


]