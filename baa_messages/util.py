import time
import math
from decimal import Decimal, getcontext
import urllib2

def get_time(time_value, precision):
    getcontext().prec = precision
    time_value = Decimal(time_value)
    time_us = int(math.floor(time_value * Decimal(1e6)))
    remainder = int(math.floor(time_value * Decimal(1e6) - Decimal(time_us)))
    return time_us, remainder


def check_internet_connection(reference):
    try:
        response=urllib2.urlopen(reference,timeout=1)
        return True
    except urllib2.URLError as err: pass
    return False