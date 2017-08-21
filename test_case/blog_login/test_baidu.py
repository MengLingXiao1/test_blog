# -*- coding: utf-8 -*-
# @Author  : Mlx
import unittest
from selenium import webdriver
class baidu_login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        print 'Testing start'

    def test_login(self):
        self.driver.get('https://www.baidu.com')
        #self.assertEqual(self.driver.title,)
        print self.driver.title

    def tearDown(self):
        self.driver.close()
        print 'Testing end'

if __name__ == "__main__":
    unittest.main()

