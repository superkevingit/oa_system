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
    g = requests.get(url + student_id, cookies=cookies)
    info = g.text
    result = json.loads(info)['result']
    username = json.loads(info)['user']['Name']
    return result, username
