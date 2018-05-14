# -*- coding:utf-8 -*-

import unittest

from common.HTMLTestRunner import HTMLTestRunner
import os
import time
import requests
import json
from Test_case.case_login import LoginCase




if __name__ == '__main__':
    # 导入HTMLTestRunner库，这句也可以放在脚本开头


    # 定义脚本标题，加u为了防止中文乱码

    report_title = u'接口测试测试报告'

    # 定义脚本内容，加u为了防止中文乱码
    desc = u'梦果商城测试报告详情：'

    # 定义date为日期，time为时间
    date = time.strftime("%Y%m%d")
    time = time.strftime("%Y%m%d%H%M%S")

    # 定义path为文件路径，目录级别，可根据实际情况自定义修改
    path = 'C:/Users/Administrator/PycharmProjects/mgcz_test/Report' + date + "/login/" + time + "/"

    # 定义报告文件路径和名字，路径为前面定义的path，名字为report（可自定义），格式为.html
    report_path = path + "report.html"

    # 判断是否定义的路径目录存在，不能存在则创建
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        pass

    # 定义一个测试容器
    testsuite = unittest.TestSuite()

    # 将测试用例添加到容器
    testsuite.addTest(LoginCase("test_login_success"))
    testsuite.addTest(LoginCase("test_hh"))

    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(report_path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)

    # 关闭report，脚本结束
    report.close()
    # 关闭浏览器
