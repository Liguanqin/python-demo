# coding = utf-8

import requests

key = ''  # 客户授权key

postdata = {
    'key': key,  # 客户授权key
    'num': '3950055201640'  # 快递单号
}

url = 'http://www.kuaidi100.com/autonumber/auto'  # 实时查询请求地址

result = requests.post(url, postdata)  # 发送请求
print(result.text)  # 返回数据
