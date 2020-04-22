# -*- coding: utf-8 -*-
# @Author: jingyuexing
# @Date:   2020-04-21 18:24:20
# @Last Modified by:   jingyuexing
# @Last Modified time: 2020-04-22 18:21:27

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

def requests(method='',url='',param={}):
    req = http.request(method=method,url=url,fields=param)
    if(req.status==200):
        return json.loads(req.data.decode('utf-8'),encoding='utf-8')

def GetHotList(limit=30):
    config = api[0]
    method = config['method']
    url = config['link']
    param = {
        'limit':limit,
        "desktop":"true"
    }
    return requests(method=method,url=url,param=param)


def getUserActive(user='',limit=10):
    config = api[1]
    url = config['link'].format(user=user)
    method = config['method']
    param = {
        "limit":limit,
        'desktop':'true'
    }
    return requests(method=method,url=url,param=param)

def getAnswerComment(answerID=0,limit=20,offset=0,status='open'):
    config = api[3]
    url = config['link'].format(answersID=answerID)
    method = config['method']
    param = {
        "limit":limit,
        "offset":offset,
        "status":status
    }
    return requests(method=method,url=url,param=param)

def getUserInfo(username=''):
    if(username!=''):
        config = api[4]
        method = config['method']
        url = config['link'].format(username=username)
        param = {
            "include":"allow_message%2Cis_followed%2Cis_following%2Cfollowing_count%2Cis_org%2Cis_blocking%2Cemployments%2Canswer_count%2Cfollower_count%2Carticles_count%2Cgender"
        }
        return requests(method=method,url=url,param=param)
def getUserFollowers(username='',offset=0,limit=20):
    if(username!=''):
        config = api[5]
        method = config['method']
        url = config['link'].format(username=username)
        param = {
            "limit":limit,
            'offset':offset,
            "include":"data[*].answer_count,articles_count,gender,is_followed,following_count,is_following,badge[?(type=best_answerer)].topics"
        }
        return requests(method=method,url=url,param=param)



class User:
    userId = '' #用户id
    name = '' #名称
    fansNumber = 0 #粉丝数
    answerNumber = 0 #回答数
    following = 0  #关注的人
    articles = 0 #文章数
    face = '' #头像
    vip = False #是否是VIP
    """docstring for User"""
    def __init__(self,userName=''):
        data = getUserInfo(username=userName)
        if(data!=None):
            self.userId = data['id']
            self.articles = data['articles_count']
            self.answerNumber = data['answer_count']
            self.face = data['avatar_url_template']
            self.vip = data['vip_info']['is_vip']
            self.following = data['following_count']
            self.fansNumber = data['follower_count']

class Answer:
    """docstring for Answer"""
    answerID = 0
    def __init__(self, arg):
        pass


class Articles:
    """docstring for Articles"""
    def __init__(self, arg):
        pass
        

