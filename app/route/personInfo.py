#-*- coding: UTF-8 -*-

from flask import Blueprint
from flask import request,jsonify,json
import traceback
import sys
sys.path.append("..")
from models import customerUser
#from flask.ext.cache import Cache



personInfo_route = Blueprint('personInfo', __name__)
#cache = Cache(personInfo_route, config={'CACHE_TYPE': 'simple'})


@personInfo_route.route('/personInfo', methods=['POST'])
#@cache.cached(timeout=50, key_prefix='cached_psnInfo_')
def personInfo():
    emptyDic = {
         "friendly":"",
         "honesty":"",
         "passion":""}

    try:
        token = request.json['token']
        user = customerUser.query.filter_by(token =token).first()
        #没有用户信息
        if user is None:
             errorDic = {"state":"fail",
                         "reason":"没有此用户"}
             errorDic = dict(errorDic,**emptyDic)
             return jsonify(errorDic)

        validOrders = user.order.filter(_or('paysate = 6' , 'paystate = 2')).order_by(orderList.paydatetime.desc()).limit(30).all()
        cancelNum = 0
        freeNum = 0
        discountPrice = 0
        totalPrice = 0
        number = 0
        for item in validOrders:
            number += 1
            if item.paystate == 4:
                cancelNum += 1
            if item.discount == 0:
                freeNum += 1
            totalPrice += item.price
            discountPrice += item.payprice

        customer.friendly = 60 + freeNum / number * 40
        customer.honesty = 100 - cancelNum / number * 100
        customer.passion = 60 + (totalPrice - discountPrice) / totalPrice * 40
        db.session.commit()

        friendly = user.friendly
        honesty = user.honesty
        passion = user.passion

        state = "successful"
        reason = ""
        return jsonify({"state":state,
                     "reason":reason,
                     "friendly":friendly,
                     "honesty":honesty,
                     "passion":passion})

    except Exception, e:
        errorDic = {"state":"fail",
                    "reason":"服务器异常"}
        errorDic = dict(errorDic,**emptyDic)
        return jsonify(errorDic)
