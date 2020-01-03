#!usr/bin/python
#-*- coding:utf-8 -*-
import flask,json

from flask import request
from flask import session
from time import sleep


server = flask.Flask(__name__)


@server.route('/entryTask',methods=['get'])
def entryTask():

    """
    Flask request接口获取参数

    request.form.get("key", type=str, default=None) 获取表单数据，
    request.args.get("key") 获取get请求参数，
    request.values.get("key") 获取所有参数
    request.get_json("key")获取解析json数据格式

    :return:
    """
    a = flask.request.values.get('a')
    b = flask.request.values.get('b')

    try:

        if a and b:
            # 移除首尾空格
            a = a.strip()
            b = b.strip()
            try:
                a=int(a)
                try :

                    if float(b) or int(b):
                        resu = {'err_code': 21, 'err_message': 'empty or wrong params'}
                        return json.dumps(resu, ensure_ascii=False)

                except Exception as e:
                    resu = {'err_code': 0, 'err_message': 'success', 'reference': outp(a, b)}
                    return json.dumps(resu, ensure_ascii=False)


            except Exception as e:

                resu = {'err_code':21,'err_message':'empty or wrong params'}
                return json.dumps(resu,ensure_ascii=False)
        else:
            resu = {'err_code': 21, 'err_message': 'empty or wrong params'}
            return json.dumps(resu, ensure_ascii=False)
    except Exception as e:
        resu = {'err_code': 11, 'err_message': 'system error'}
        return json.dumps(resu, ensure_ascii=False)


def outp(a,b):
    result_str="NO.%s is %s"%(a,b)
    return result_str


if __name__ == '__main__':
    server.run(debug=False,threaded=True,port=5000,host='0.0.0.0')
