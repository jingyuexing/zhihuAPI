# -*- coding: utf-8 -*-
# @Author: jingyuexing
# @Date:   2020-04-21 18:24:20
# @Last Modified by:   jingyuexing
# @Last Modified time: 2020-04-21 20:30:06

import json
import urllib3
http  =urllib3.PoolManager()

head = {
  "Sec-Fetch-Mode":"no-cors",
  "Cache-Control":"max-age=0",
  "Accept-Encoding":"gzip, deflate, br",
  "Accept-Language":"zh-CN,zh;q=0.9",
  "Accept":"application/json, text/plain, */*",
  "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

with open('data/API.json','r',encoding='utf-8') as file:
    api = json.loads(file.read())
    file.close()

def requests(method='',url='',parma={}):
    req = http.request(method=method,url=url,parma=parma)
    if(req.status==200):
        return json.loads(req.data.decode('utf-8'),encoding='utf-8')

def GetHotList(limit=30):
    config = api[0]
    method = config['method']
    url = config['link']
    parma = {
        'limit':limit,
        "desktop":"true"
    }
    return requests(method=method,url=url,parma=parma)


def getUserActive(user='',limit=10):
    config = api[1]
    url = config['link'].format(user=user)
    parma = {
        "limit":limit,
        'desktop':'true'
    }
    return requests(method=method,url=url,parma=parma)

def getAnswerComment(answerID=0,limit=20,offset=0,status='open'):
    config = api[3]
    url = config['link'].format(answersID=answerID)
    method = config['method']
    parma = {
        "limit":limit,
        "offset":offset,
        "status":status
    }
    return requests(method=method,url=url,parma=parma)


class User:
    userId = ''
    name = ''
    fansNumber = 0
    answerNumber = 0
    articles = 0
    vip = False
    """docstring for User"""
    def __init__(self,userName=''):
        pass


class Answer:
    """docstring for Answer"""
    answerID = 0
    def __init__(self, arg):
        pass


class Articles:
    """docstring for Articles"""
    def __init__(self, arg):
        pass
        
                        