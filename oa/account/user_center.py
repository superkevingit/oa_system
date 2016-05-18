# encoding: utf-8
import requests
import json


def login_post(url, data):
    r = requests.post(url, data=data)
    msg = r.text
    token = json.loads(msg)['token']
    result = json.loads(msg)['result']
    return result, token


def get_info(url, token, student_id):
    cookies = dict(uc_token=token)
    url = url + student_id
    g = requests.get(url, cookies=cookies)
    info = g.text
    info = json.loads(info)
    result = info['result']
    username = info['user']['Name']
    return result, username
