# -*- coding: utf-8 -*-
# @Time    : 2019-12-30 15:52
# @Author  : Seven
# @File    : RedisExList.py
# @Desc    : Redis过期列表


import datetime
import time

import redis


class RedisExList:
    """ Redis过期列表 """

    def __init__(self, expiration=30):
        self.redis = redis.Redis.from_url('REDIS_EX_LIST_URL')
        self.expiration = expiration

    def get_value(self, key):
        """ 获取value并删除 """
        self.delete_expiration_value(key)
        value_list = self.redis.zrange(key, 0, 0, withscores=True)
        if not value_list:
            return
        value = value_list[0][0].decode()
        self.redis.zrem(key, value)
        return value

    def set_value(self, key, value):
        """ 设置value"""
        self.delete_expiration_value(key)
        return self.redis.execute_command('ZADD', key, time.time(), value)

    def delete_expiration_value(self, key):
        """ 过期value"""
        overdue_day = (datetime.datetime.now() - datetime.timedelta(seconds=self.expiration)).timestamp()
        return self.redis.zremrangebyscore(key, 0, overdue_day)

    def delete_value(self, key, value):
        """ 删除列表中指定value """
        return self.redis.zrem(key, value)

    def len(self, key):
        """ 返回列表个数 """
        self.delete_expiration_value(key)
        return self.redis.zcard(key)
