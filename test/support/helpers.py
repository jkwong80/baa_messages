import time, sys, os, random
from baa_messages.util import get_time

def random_coordinate():
    return random.randint(73, 100) + random.random()/100

def random_coordinates():
    return [random_coordinate(), random_coordinate()]

def formatted_time(time=time.time()):
    # The get_time methods provides the time in us and remainder as per the schema
    return get_time(time)

