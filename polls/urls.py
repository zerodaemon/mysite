# coding=utf-8
from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$',          # 表示空值
        views.index,    # 对应view中定义的index
        name='index'),  # 名字，用于在模板中调用


    # ex: /polls/5/     # 将用户输入URL中的id通过正则传入question_id，然后再传入view中的detail函数
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)