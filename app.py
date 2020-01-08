# -*-coding:utf-8 -*-
import flask,json
from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/entryTask',methods=['get'])
def entryTask():


     a = flask.request.values.get('a')
     b = flask.request.values.get('b')

     try:

          a = a.strip()
          b = b.strip()
          a = int(a)

          if b:
              resu = {'err_code': 0, 'err_message': 'success','reference':outp(a,b)}
              return json.dumps(resu, ensure_ascii=False)

          else:
              resu = {'err_code': 21, 'err_message': 'empty or wrong params'}
              return json.dumps(resu, ensure_ascii=False)

     except Exception as e:
          resu = {'err_code': 21, 'err_message': 'empty or wrong params'}
          return json.dumps(resu, ensure_ascii=False)


def outp(a,b):
    result_str="NO.%s is %s"%(a,b)
    return result_str



if __name__ == '__main__':
     app.run(debug=True,port=5000,host='0.0.0.0')
