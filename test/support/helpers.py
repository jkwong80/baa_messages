import time, sys, os, random

def random_coordinate():
    return random.randint(73, 100) + random.random()/100

def random_coordinates():
    return [random_coordinate(), random_coordinate()]

