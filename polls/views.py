# coding=utf-8
from django.http import HttpResponse
from polls.models import Question
from django.http import Http404
from django.shortcuts import render
# from django.template import RequestContext, loader


def detail(request, question_id):   # id来源于urls
    try:
        question = Question.objects.get(pk=question_id)  # 通过Question模型，传入问题id，获取问题
    except Question.DoesNotExist:   # 一旦不存在
        raise Http404               # 返回404页面
    return render(request, 'polls/detail.html', {'question': question})  # 三个参数，request对象，模板，字典

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)  # 类似print的函数

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]   # 读取最近发布的5个问题

    # template = loader.get_template('polls/index.html')  # 调用模板
    # context = RequestContext(request, {
    #     'latest_question_list': latest_question_list,
    # })
    # return HttpResponse(template.render(context))

    context = {'latest_question_list': latest_question_list} # 制作字典
    return render(request, 'polls/index.html', context)