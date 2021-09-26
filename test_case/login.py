import requests

from configs.config import Host
import hashlib


# md5加密
def get_Md5(password):
    # 实例化
    md5 = hashlib.md5()
    # 进行加密
    md5.update(password.encode('utf-8'))
    # 返回加密结果
    return md5.hexdigest()


class Login:

    def login(self, indatqa):
        url = f'{Host}/account/sLogin'
        # rqby = {'username': 'dp0367', 'password': '07f39c7a8ed35cf0a867db25788f30c1'}

        indatqa['password'] = get_Md5(indatqa['password'])
        rqby = indatqa

        resp = requests.post(url, data=rqby)
        # 打印请求体
        print(resp.request.body)

        # 打印text格式响应体
        # print(resp.text)

        # 获取token 值
        print('token值为：' + resp.json()['data'].get('token'))

        # 打印字典 格式响应体 前提个是必须是json格式的否则报错
        return resp.json()


if __name__ == '__main__':
    res = Login().login({'username': 'dp0367', 'password': '42956'})
    print(res)
