#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]