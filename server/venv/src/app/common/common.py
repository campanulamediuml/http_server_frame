import datetime
import time
import config
import hashlib
import json
from app.data.server import Data
from common import daily_mission


# 时间戳转2018-01-01 8:00:00
def time_to_str(times=time.time()):
    date_array = datetime.datetime.utcfromtimestamp(times+(8*3600))
    return date_array.strftime("%Y-%m-%d %H:%M:%S")


# 获取md5
def get_md5(string):
    md5 = hashlib.md5(string.encode('ascii')).hexdigest()
    return md5