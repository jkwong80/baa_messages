import time
import math
from decimal import Decimal, getcontext,ROUND_FLOOR
import urllib2

def get_time(timestamp_seconds):
    return int(math.floor(float(timestamp_seconds)*1e6))


def check_internet_connection(reference):
    try:
        response = urllib2.urlopen(reference,timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False