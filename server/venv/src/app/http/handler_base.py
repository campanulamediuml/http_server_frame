from tornado.web import RequestHandler

from app.http.error_code import ERROR_CODE

from app.data.server import Data

import json


class HandlerBase(RequestHandler):

    
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.set_header('Access-Control-Max-Age', 1000)
        self.set_header('Access-Control-Allow-Headers', '*')

    def get_result(self):
        '''
        返回结构基本模板
        :return:
        '''
        result = {}
        result['status'] = 0
        result['msg'] = ''
        result['data'] = {}
        return result

    def get_user_base(self):
        '''
        获取用户基本信息
        :return:
        '''
        token = self.get_argument('token')
        print(token)
        conditions = []
        conditions.append(('token', '=', token))

        user_data = Data.find(Data.USER, conditions)
        
        return user_data


        # return user_data


    def send_ok(self, data = {}):
        '''
        正确信息返回
        :param data:
        :return:
        '''
        result = self.get_result()
        result['data'] = data
        self.write(result)

    def send_faild(self, code):
        '''
        失败信息返回
        :param code:
        :return:
        '''
        result = self.get_result()
        unit = ERROR_CODE[code]
        result['status'] = unit[0]
        result['msg'] = unit[1]
        self.write(json.dumps(result))

    def get_data(self):
        '''
        获取请求内容
        :return:
        '''
        data = self.get_argument('data')
        res = json.loads(data)
        return res
