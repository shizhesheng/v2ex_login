# -*- coding: utf-8 -*-
import os


def get_project_path():
    """
    获取项目绝对路径
    :return:
    """
    project_name = '/v2ex_login/v2ex_login'
    file_path = os.path.dirname(__file__)

    return file_path[:file_path.find(project_name) + len(project_name)]


def sep(path, add_sep_before=False, add_sep_after=False):
    """
    前后加分隔符
    :param path: 新增的是列表[]
    :param add_sep_before:
    :param add_sep_after:
    :return:
    """
    all_path = os.sep.join(path)
    if add_sep_before:
        all_path = os.sep + all_path
    if add_sep_after:
        all_path = all_path + os.sep
    return all_path
