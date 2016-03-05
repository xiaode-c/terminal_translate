#!/usr/bin/python
#encoding:utf-8

import json
import requests
import sys

#下面两个是有道翻译api提供，可以到有道翻译申请API
API_KEY = <your_apikey>
KEYFROM = <your_keyfrom>

API_URL = 'http://fanyi.youdao.com/openapi.do'

#使终端输出带颜色的字
red = '\033[31;1m %s \033[1;m'
green = '\033[32;1m %s \033[1;m'
blue = '\033[34;1m %s \033[1;m'
purple = '\033[35;1m %s \033[1;m'
yellow = '\033[33;1m %s \033[1;m'
dark_green = '\033[36;1m %s \033[1;m'

def getTranslate(text):
    myurl = API_URL+'?keyfrom='+KEYFROM+'&key='+API_KEY+'&type=data&doctype=json&version=1.1&q='+text
    response = requests.get(myurl).text
    json_text = json.loads(response)
    if not json_text.has_key("basic"):
        print red % "未查询到该词！！！"
    else:
        print dark_green % u"单词：\n\t" + green % json_text["query"]
        for tl in json_text["translation"]:
            print dark_green % u"翻译：\n\t"+ blue % tl

        print dark_green % "详细："
        for exp in json_text["basic"]["explains"]:
            print "\t" + blue % exp

        print dark_green % "网络短语："
        for i in json_text["web"]:
            print "\t"+yellow % i["key"],
            for j in i["value"]:
                print blue % j,
            print ""

text = sys.argv[1]
getTranslate(text)
