#!/usr/bin/python3
# _*_ coding: utf-8 _*_
# @Time    : 2020/2/6 15:42
# @Author  : Leon Zhou
# @Email   : zx-leon@163.com
# @File    : adminx.py
# @Software: PyCharm
import xadmin

from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = [
        'name',
        'desc',
        'fav_nums',
        'image',
        'click_nums',
        'address',
        'city']
    search_fields = [
        'name',
        'desc',
        'fav_nums',
        'image',
        'click_nums',
        'address',
        'city']
    list_filter = [
        'name',
        'desc',
        'fav_nums',
        'image',
        'click_nums',
        'address',
        'city']


class TeacherAdmin(object):
    list_display = [
        'org',
        'name',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'fav_nums',
        'click_nums',
        'add_time']
    search_fields = [
        'org',
        'name',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'fav_nums',
        'click_nums']
    list_filter = [
        'org',
        'name',
        'work_years',
        'work_company',
        'work_position',
        'points',
        'fav_nums',
        'click_nums',
        'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
