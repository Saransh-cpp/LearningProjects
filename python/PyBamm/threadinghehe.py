import time
import signal

# https://stackoverflow.com/a/51286699/14746647
# class TimeoutException(Exception):   # Custom exception class
#     pass


# def break_after(seconds=2):
#     def timeout_handler(signum, frame):   # Custom signal handler
#         raise TimeoutException
#     def function(function):
#         def wrapper(*args, **kwargs):
#             signal.signal(signal.SIGALRM, timeout_handler)
#             signal.alarm(seconds)
#             try:
#                 res = function(*args, **kwargs)
#                 signal.alarm(0)      # Clear alarm
#                 return res
#             except TimeoutException:
#                 time.sleep(10)
#                 print('Oops, timeout: %s sec reached.' % seconds, function.__name__, args, kwargs)
#                 time.sleep(10)
#                 test(1, 2, 3)
#             return
#         return wrapper
#     return function

# @break_after(2)
# def test():
#     while True:
#         try:
#             print(dome())
#             time.sleep(10)
#         except Exception as e:
#             print(e)

def dome():
    return 1

import multiprocessing

def test(f=False):
    while True:
        try:
            print(dome())
            time.sleep(10)
        except Exception as e:
            print(e)

def call():
    p = multiprocessing.Process(target=test)
    p.start()
    p.join(5)

    if p.is_alive():
        print("KIL")
        p.kill()

call()

