# -*- coding:utf-9 -*-
import scrapy
import urllib.request

from scrapy.http import Request, FormRequest


class LoginSpider(scrapy.Spider):
    name = 'login'
    allowed_domains = ["douban.com"]
    # 设置头信息变量，供下面的代码中模拟成浏览器爬取
    header = {"User-Agent": "****"}

    # 编写start_requests()方法，第一次回默认调取该方法中的请求
    def start_requests(self):
        # 首先爬一次登录页，然后进入回调函数parse
        return [Request("http://**/login", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        # 获取验证码图片所在地址，获取后赋给captcha变量，此时captcha为一个列表
        captcha = response.xpath("**").extract()
        # 因为登录时有时需要网页有验证码，有时网页没有验证码，所以需要判断此时是否需要输入验证码
        # 若captcha列表中有元素，说明有验证码信息
        if len(captcha) > 0:
            print("此时有验证码")
            # 设置将验证码图片存储到本地的本地地址
            local_path = "***/captcha.png"
            # 将服务器中的验证码图片存储到本地，供我们在本地直接进行查看
            urllib.request.urlretrieve(captcha[0], filename=local_path)
            print("请查看本地图片captcha.png并输入对应验证码：")
            # 通过input()等待我们输入对应的验证码并赋给captcha_value变量
            captcha_value = input()
            # 设置要传递的post信息
            data = {
                # 设置登录账号，格式为账号字段名：具体账号
                "form_email": "****",
                # 设置密码
                "form_password": "****",
                # 设置验证码
                "captcha": captcha_value,
                # 设置需要转向的网址
                "redir": "****",
            }
        # 否则说明captcha列表中没有元素，即此时不需要输入验证码信息
        else:
            print("此时没有验证码")
            # 设置要传递的post信息，此时没有验证码字段
            data = {
                "form_email": "****",
                "form_password": "****",
                "redir": "****",
            }
        print("登录中……")
        # 通过FormRequest.from_response()进行登录
        return [FormRequest.from_response(response,
                                          # 设置cookie信息
                                          meta={'cookiejar': response.meta["cookiejar"]},
                                          # 设置headers信息模拟成浏览器
                                          headers=self.header,
                                          # 设置post表单中的数据
                                          formdata=data,
                                          # 设置回调函数，此时回调函数为next
                                          callback=self.next, )]

    def next(self, response):
        pass
