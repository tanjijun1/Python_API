import pytest
import allure
import requests
import json
import time

from Common import Post
from Common import Get
from Common import Assert
from Common import Consts

from message_verb.login import off_login


class Reply:
#userId_S关注userId_M
    def off_reply(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:2999/v1/share/reply/add'
        params = {'token':'12345678901234567890123456789012', 'commentId':'40719', 'content':'enenen2','target':3344}

        tokenData = off_login()
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)
        print(res)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


#userId_S取消关注userId_M
    def off_unfollow(self):
        sessionX = requests.session()
        post_req = Post.Post()
        ass = Assert.Assertions()

        url = 'http://47.99.180.185:2999/v1/user/unfollow'
        params = {'token':'12345678901234567890123456789012', 'to':'1340135'}

        tokenData = off_login()
        params['token'] = tokenData

        res = post_req.post_model_b(sessionX, url, params)

        resCode = res['code']
        resText = res['text']

        assert ass.assert_code(resCode, 200)
        assert ass.assert_in_text(resText, '成功')
        Consts.RESULT_LIST.append('True')


if __name__ == "__main__":
    test = Reply()
    #test.off_follow()
    test.off_reply()

