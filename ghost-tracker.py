import time
from datetime import datetime

def timestamp_to_readable(ts):
    return datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S UTC')

def now_unix():
    return int(time.time())

