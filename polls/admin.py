# coding=utf-8
from django.contrib import admin
from polls.models import Question, Choice

#class ChoiceInline(admin.StackedInline):  # 以
class ChoiceInline(admin.TabularInline):  # 定义内联对象，以表格方式显示内嵌有关联对象
    model = Choice  # 指定模型名字
    extra = 3  # 默认显示多少个


class QuestionAdmin(admin.ModelAdmin):  # 提问模型的管理对象

    inlines = [ChoiceInline]            # 将答案作为内联对象引入
    fieldsets = [                       # 设置答案的字段分组
        ('Question Name',    {'fields': ['question_text']}),                      # 第一组：问题内容
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),  # 第二组：问题的发布日期，折叠
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 列表视图，以及显示的字段
    list_filter = ['pub_date']         # 增加右边栏快速过滤器
    search_fields = ['question_text']  # 增加搜索功能

admin.site.register(Question, QuestionAdmin)  # 注册提问模型，将提问模型的管理对象作为参数传入
