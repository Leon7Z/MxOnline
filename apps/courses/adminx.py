#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time    : 2020/2/6 14:34
# @Author  : Leon Zhou
# @Email   : zx-leon@163.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin

from .models import Course, CourseResource, Lesson, Video


class CourseAdmin(object):
    list_display = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_time',
        'students',
        'fav_nums',
        'image',
        'click_nums',
        'add_time']
    search_fields = [
        'name',
        'desc',
        'detail',
        'degree',
        'students',
        'fav_nums',
        'click_nums']
    list_filter = [
        'name',
        'desc',
        'detail',
        'degree',
        'learn_time',
        'students',
        'fav_nums',
        'click_nums',
        'add_time']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['course', 'name', 'download']
    list_filter = ['course', 'name', 'download', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
