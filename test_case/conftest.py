# encoding: utf-8
import pytest
import allure
import yaml
import os
# from utils import get_file_path
'''
@author: lingshu
@file: conftest.py
@time: 2019/6/6 11:10
@desc:
'''
@pytest.fixture(scope="session",autouse=True)
def env_config(request):
    """
    读取yml配置文件
    """
    project_name = 'api_auto_test'
    rootPath = get_root_path()
    print(rootPath)
    config_path = os.path.abspath(rootPath + 'config/env_config.yml')  # 获取tran.csv文件的路径
    with open(config_path) as f:
        env_config = yaml.load(f) #读取配置文件
    return env_config

# def get_root_path(project_name):
#     curPath = os.path.abspath(os.path.dirname(__file__))
#     rootPath = curPath[:curPath.find(project_name+"/") + len(project_name+"/")]  # 获取myProject，也就是项目的根路径
#     return rootPath

def get_root_path():
    '''
    获取根路径
    :param project_name: 项目名
    :return:
    '''
    curPath = os.path.abspath(os.path.dirname(__file__))
    rootPath = curPath[:curPath.find("test_case")-1]+"/"  # 获取myProject，也就是项目的根路径
    print(rootPath)
    # print("rootPath= %s",rootPath)
    return rootPath
