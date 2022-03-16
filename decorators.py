# def my_decorator(func):
#     def wrapper():
#         print("ÖNCE")
#         func()
#         print("SONRA")
#     return wrapper

# @my_decorator
# def sayhello():
#     print("hello")

# sayhello()

# # sayhello = my_decorator(sayhello)          
# # sayhello()

import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+ str(finish-start)+" "+ " saniye sürdü")
    return inner
@calculate_time
def usalma(a,b):
    print(math.pow(a,b))

@calculate_time   
def faktoriyel(num):
    print(math.factorial(num))


usalma(3,4)
faktoriyel(5)