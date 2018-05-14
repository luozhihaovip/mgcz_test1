import json
import unittest
import requests


http_headers = { 'Accept': '*/*','Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'}
Session = requests.session()
rr = Session.get('http://mall.mengguochengzhen.cn/mgcz/system/',headers=http_headers)

print(rr.url)




def get_real_url(url):
    rs = requests.get(url,headers=http_headers,timeout=10)
    rs.url

# class LoginCase(unittest.TestCase):
#     # 定义登录方法，被测试用例调用
#     def setUp(self):
#         # 需要测试的网页
#         self.url = 'http://mall.mengguochengzhen.cn/mgcz/mobi/promotion/getPromotionCommodity?promotionId=32694c26639d484fa032bcdb3b45e114&pageNO=5'
#         # 定义测试方法，框架中测试方法以test_开头，底下引号中的中文会在报告中显示，利于清楚的知道测试目的
#     def test_login_success(self):
#         '''coding'''
#         r = requests.post(self.url)
#         # 解码json格式数据
#         dicts = json.loads(r.text)
#         code = r.status_code
#         # 对比返回值
#         self.assertEqual(code, 200)
#         self.assertEqual(dicts['status'], 1)
#
#     def test_hh(self):
#         '''test'''
#         self.assertEqual(1,'1')