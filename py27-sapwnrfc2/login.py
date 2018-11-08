#!/usr/bin/env python
import os, sys
from pyrfc import Connection, ABAPApplicationError, ABAPRuntimeError, LogonError, CommunicationError
from backports import configparser
import configparser
import json
from pprint import PrettyPrinter
from pyrfc import Connection
from pyrfc import *

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

conn = Connection(ashost='vcenbpcdev01.petronas.com.my', sysnr='01', client='500', user='andrew', passwd='Fitnessfirst@1')
config = configparser.ConfigParser()
#pp = PrettyPrinter(indent=4)
#options = [{ 'TEXT': "FCURR = 'USD'"}]


#pp.pprint(result['DATA'])

@app.route('/getall',methods=['GET'])
def getAllEmp():
    result = conn.call('BAPI_USER_GET_DETAIL',
                     USERNAME = 'andrew',
                     CACHE_RESULTS  = ' ')
    # if isinstance(result, bytes):
    print(result['ADDRESS'])
    return jsonify(result['ADDRESS'])

@app.route('/getTab',methods=['GET'])
def getTab():
    ROWS_AT_A_TIME = 4
    rowskips = 0
    result = conn.call('RFC_READ_TABLE', \
                                QUERY_TABLE = 'ZBPC_COE_MD', \
                                ROWSKIPS = rowskips, ROWCOUNT = ROWS_AT_A_TIME)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
