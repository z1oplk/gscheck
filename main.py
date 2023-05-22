import requests
import json
import os

def main():
    
    url = os.environ.get("gsurl") # 发送POST请求的网址
    cookie = os.environ.get("gs_ck") # 修改为你的cookie
    gktk = os.environ.get("gktk")
    ddtk = os.environ.get("ddtk")
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36' # 修改为你的useragent

    # 构造POST请求的参数
    payload = {'token': gktk}

    # 构造请求头部
    headers = {'Cookie': cookie, 'User-Agent': user_agent}

    # 发送POST请求
    response = requests.post(url, data=payload, headers=headers)

    # 解析JSON数据
    response_json = json.loads(response.text)

    # 获取message值
    message = response_json.get('message', '')
    
    print(message)
    
    # 构造钉钉机器人webhook的请求体
    data = {
        'msgtype': 'text',
        'text': {
            'content': message
        }
    }

    # 发送钉钉机器人webhook请求
    webhook_url = 'https://oapi.dingtalk.com/robot/send?access_token=' + ddtk
    response = requests.post(webhook_url, json=data)

    # 输出响应内容
    print(response.text)

if __name__ == '__main__':
    main()
