# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^polls/',             # 以polls/的地址开头的正则表达式
        include('polls.urls', namespace="polls")), # 引用polls应用中的urls文件
    url(r'^admin/', include(admin.site.urls)),
)