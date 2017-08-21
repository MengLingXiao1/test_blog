# -*- coding: utf-8 -*-
# @Author  : Mlx
import unittest
import time
import HTMLTestRunner
import os

def add_case(casePath,rule):
    '''加载所有用例'''
    testunit=unittest.TestSuite()
    discover= unittest.defaultTestLoader.discover(case_path,pattern=rule,top_level_dir=None)
    # for test_case in discover:
    #     print test_case
    testunit.addTest(discover)
    return testunit

def run_case(all_case,report_path):
    """执行所用用例并写入测试报告"""
    now=time.strftime('%Y_%m_%d %H_%M_%S')
    report_abspath=os.path.join(report_path,now+'result.html')
    fp=open(report_abspath,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'自动化测试报告',description=u'用例执行情况')
    runner.run(all_case)
    fp.close()

if __name__=="__main__":
    #测试用例路径
    case_path=r'H:\Git\test_blog\test_case'
    rule='test*.py'
    all_case=add_case(case_path,rule)
    #生成测试报告
    report_path=r'H:\Git\test_blog\test_report'
    run_case(all_case,report_path)
