import json
import time
import random

import requests

headers = {
    'Host': 'bocfz.sinodoc.cn:8099',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
    'token': '',
    'Content-Type': 'application/json',
    'Origin': 'https://bocfz.sinodoc.cn',
    'Referer': 'https://bocfz.sinodoc.cn/',
}




# 获取token
def kfx_sign():
    url = 'https://bocfz.sinodoc.cn:8099/api/UniLogin/bocCryptAllLogin'
    data = {
        "cipherText": "{\"hmaCipherText\":\"0682f7b10cb7b19b776c6937e2da7417ec3db2a6c6d994cf282b15b2afdbc917\",\"hmac\":\"3045022100cc5e5e95287705b3762320fa86035321bf3862b0a7e6a388fe072689f5cab63802202e210bf8a8b0d07a3cb79ad8526a672e68255c1d3dc64cdfc349865bc1fff2eb\",\"skey\":\"BDQfgIKMjD8fS2qNivp7RXH4ExpdoA5g1TDrT/G2t4WdKd+LgZV82IWVtdkP7cvV/6ByPosw02kuPpMSXYY08/EAHPgkgP2AZ1bf63Mndy/fyuxY+u/hvOLImJ8zFW6bjwlFUU1r48BC9nAYI3L3vXE5RYlsTwi6pCOGI6RwJW9C\",\"body\":\"f51a501b07eee7b4d21889e3cd511af41383e11bd7885b6567e761012a3c90659d65c3ca93687661c06a162590737776e7753e026de02b2b23e9c1a861a370abb6bc2ed612bb4334b145d96ce026afb73366e329c8bc5598f848b933beee0f1b1e733a7edf450375fb5a3edc3b34cb27621f3070395d9e4b40dde6cff47a11524d5566ac4a0314524a4989d7ac5703fde100da3a851052cb545fde0acbe47c84a1c1a06aa62eed5ef92213cc3bd0d6bd307fffd3d39f0585422d06011238b0c509ed3160441432a827f30ba2190de6a24b9d0349e671d20c7faa89cb9ffc296b92627444b279df4684f3c7449505d17d4d20694793c9c8eaf5f6ff32e8d3936fa141eff24e0b31a9bde0aa534ba83ecd\"}",
        "login_level": "4"
    }
    body = json.dumps(data).encode(encoding='utf-8')
    response = requests.post(url=url, headers=headers, data=body).json()
    print(str(response))
    if response["code"] == "200":
        return response["data"]["token"]
    else:
        print(response["msg"])


# 获取任务列表
def get_tasks(token):
    url = 'https://bocfz.sinodoc.cn:8099/api/Tasks/allTaskLists'
    data = {
        "channel": "boc"
    }
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    body = json.dumps(data).encode(encoding='utf-8')
    response = requests.post(url=url, headers=headers, data=body).text
    json_dicti = json.loads(response)
    if json_dicti["code"] == "200":
        json_dicti = json_dicti['data']
        langs = []
        for key in json_dicti:
            if (json_dicti[key]['type'] == 5) & (json_dicti[key]['state'] == 0):
                langs.append(int(json_dicti[key]['id']))
        return langs
    else:
        print(response["msg"])


def click_tasks(ids):
    url = 'https://bocfz.sinodoc.cn:8099/api/Tasks/clickTaskBotm'
    for x in ids:
        time.sleep(1)
        data = {'taskid': x, 'state': 0}
        headers = {
            'Authorization': token,
            'Host': 'bocfz.sinodoc.cn:8099',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
            'Content-Type': 'application/json',
            'Origin': 'https://bocfz.sinodoc.cn',
            'Referer': 'https://bocfz.sinodoc.cn/',
        }
        body = json.dumps(data)
        response = requests.post(url=url, headers=headers, data=body).json()
        if response["code"] == "200":
            print(str(response) + "————————任务点击" + str(x))
            tasks_detail(x)
        else:
            print(response["msg"])
    if ids != []:
        pushplus_bot("中行任务完成！", "中行任务完成！")


def tasks_detail(id):
    url = 'https://bocfz.sinodoc.cn:8099/api/Tasks/taskDetail'

    data = {'tid': id, 'channel': "boc"}
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    body = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=body).json()
    if response["code"] == "200":
        print(str(response) + "————————任务点击" + str(id))
    else:
        print(response["msg"])


def to_user_tasks():
    url = 'https://bocfz.sinodoc.cn:8099/api/Tasks/toUserHoustTask'
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    response = requests.post(url=url, headers=headers).json()


def chaenge_prop():
    my_json_dicti = local_specialty(0)
    my_list = []
    # 我的
    for key in my_json_dicti:
        if (key['type'] != 300) & (key['lock'] == 0):
            # 锁定
            print("锁定纪念品成功")
            lock_prod(key['id'])
            print(key)
        else:
            my_list.append((key['id']))

    # 好友
    my_prop = 0
    if my_list != []:
        my_prop = random.choice(my_list)
    frid_list = []
    frid_json_dicti = local_specialty(780461)
    for key in frid_json_dicti:
        if (key['type'] > 300) & (key['lock'] == 0):
            # 锁定
            print('好友的珍贵的' + str(key))
            frid_list.append((key['id']))
    frid_prop = 0
    if frid_list != []:
        frid_prop = random.choice(frid_list)

    url = 'https://bocfz.sinodoc.cn:8099/api/UserProps/changePropByFriend'
    data = {"self_prop_id": my_prop, "frid_prop_id": frid_prop, "fuid": 780461}
    if my_prop != 0 & frid_prop != 0:
        headers = {
            'Authorization': token,
            'Host': 'bocfz.sinodoc.cn:8099',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
            'token': '',
            'Content-Type': 'application/json',
            'Origin': 'https://bocfz.sinodoc.cn',
            'Referer': 'https://bocfz.sinodoc.cn/',
        }
        body = json.dumps(data)
        response = requests.post(url=url, headers=headers, data=body).text
        json_dicti = json.loads(response)
        if json_dicti["code"] == "200":
            print(json_dicti["msg"])
            print("交换成功")
            pushplus_bot("交换成功", "交换成功")
        else:
            print(json_dicti["msg"])


# 获取自己的纪念品
def local_specialty(fuid):
    url = 'https://bocfz.sinodoc.cn:8099/api/UserProps/localSpecialty'

    data = {"fuid": fuid, "last_id": 0}
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    body = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=body).text
    json_dicti = json.loads(response)
    if json_dicti["code"] == "200":
        json_dicti = json_dicti['data']['lists']
        return json_dicti


def lock_my():
    my_json_dicti = local_specialty(0)
    my_list = []
    # 我的
    for key in my_json_dicti:
        if (key['type'] != 300) & (key['lock'] == 0):
            # 锁定
            print("锁定纪念品成功")
            lock_prod(key['id'])
            print(key)
        else:
            my_list.append((key['id']))

# 锁定
def lock_prod(propId):
    url = 'https://bocfz.sinodoc.cn:8099/api/UserProps/lockProd'

    data = {"prop_id": propId, "lock": 1}
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    body = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=body).text
    json_dicti = json.loads(response)
    if json_dicti["code"] == "200":
        print("锁定成功" + json_dicti["msg"])
    else:
        print(json_dicti["msg"])


# 旅行
def begin_tour():
    url = 'https://bocfz.sinodoc.cn:8099/api/UserTour/beginTour'

    data = {"timer": "train", "city_id": random.choice(get_city()), "type": "TOUR", "friend_id": 0}
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    body = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=body).text
    json_dicti = json.loads(response)
    if json_dicti["code"] == "200":
        print("开始旅行" + json_dicti["msg"])
        to_answer()
    else:
        print(json_dicti["msg"])


# 获取旅游城市
def get_city():
    url = 'https://bocfz.sinodoc.cn:8099/api/UserCitys/config'

    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    # body = json.dumps(data)
    citys = []
    response = requests.post(url=url, headers=headers).text
    json_dicti = json.loads(response)
    if json_dicti["code"] == "200":
        for key in json_dicti['data']['area1']:
            if (key['bx_l']) != 0:
                citys.append(key['city_id'])
                print("有奖的城市" + key['city'])
        if not citys:
            citys.append(1)
        return citys
    else:
        print(json_dicti["msg"])


# 答题
def init_answer():
    url = 'https://bocfz.sinodoc.cn:8099/promotion/tourAnswer/initData'

    data = {}
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    body = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=body).text
    json_dicti = json.loads(response)
    if json_dicti["code"] == "200":
        print("开始答题" + json_dicti["msg"])
        return json_dicti['data']['tour_answer_id']
    else:
        print(json_dicti["msg"])


# 获取答题
def get_answer():
    url = 'https://bocfz.sinodoc.cn:8099/promotion/tourAnswer/question'
    tour_answer_id = init_answer()
    data = {"tour_answer_id": tour_answer_id}
    headers = {
        'Authorization': token,
        'Host': 'bocfz.sinodoc.cn:8099',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
        'token': '',
        'Content-Type': 'application/json',
        'Origin': 'https://bocfz.sinodoc.cn',
        'Referer': 'https://bocfz.sinodoc.cn/',
    }
    questions = []
    body = json.dumps(data)
    response = requests.post(url=url, headers=headers, data=body).text
    json_dicti = json.loads(response)
    if json_dicti["code"] == "200":
        print("开始答题" + json_dicti["msg"])
        for key in json_dicti['data']['question']:
            print(key)
            questions.append(key['id'])
        return questions
    else:
        print(json_dicti["msg"])


# 提交答题
def to_answer():
    url = 'https://bocfz.sinodoc.cn:8099/promotion/tourAnswer/answerResult'
    tour_answer_id = init_answer()
    questions = get_answer()

    for index, key in enumerate(questions):
        data = {
            "result": 1,
            "question_id": key,
            "tour_answer_id": tour_answer_id,
            "progress": index
        }
        headers = {
            'Authorization': token,
            'Host': 'bocfz.sinodoc.cn:8099',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 bocapp(7.6.0);lsta:4;;cifNumber:490912841;;sessionId:93a80007-88c4-4950-b558-b3ad7083c1b1_encry;;appSequence:20900;',
            'token': '',
            'Content-Type': 'application/json',
            'Origin': 'https://bocfz.sinodoc.cn',
            'Referer': 'https://bocfz.sinodoc.cn/',
        }
        body = json.dumps(data)
        response = requests.post(url=url, headers=headers, data=body).text
        json_dicti = json.loads(response)
        if json_dicti["code"] == "200":
            print("开始答题" + json_dicti["msg"])
        else:
            print(json_dicti["msg"])


def xxxxx():
    url = 'https://bocfz.sinodoc.cn:8099/api/UserInfo/detail'
    response = requests.get(url=url, headers=headers).json()
    if response["error_code"] == 0:
        nickname = response["data"]["nickname"]
        memberBalance = response["data"]["serialSign"][0]["memberBalance"]
        print(f"账号{nickname}签到后积分{memberBalance}")
    else:
        print(response["msg"])


def pushplus_bot(title, content):
    try:
        print("\n")
        print("PUSHPLUS服务启动")
        url = 'http://www.pushplus.plus/send'
        data = {
            "token": '197ef2a6e00d4c37a1992491ebdba082',
            "title": title,
            "content": content
        }
        body = json.dumps(data).encode(encoding='utf-8')
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url, data=body, headers=headers).json()
        if response['code'] == 200:
            print('推送成功！')
        else:
            print('推送失败！')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # kfxtoken = os.environ['kfxtoken']
    # kfxtoken = kfxtoken.split('@')
    # push_token = os.environ['push_token']
    # for ck in range(len(kfxtoken)):
    #     number = ck + 1
    #     headers1 = {
    #         'token': kfxtoken[ck]
    #     }
    #     headers.update(headers1)
    # kfx_getUserInfo1(number, push_token)
    token = kfx_sign()
    ids = get_tasks(token)
    click_tasks(ids)
    to_user_tasks()
    begin_tour()
    # chaenge_prop()
    lock_my()

    # kfx_getUserInfo()
