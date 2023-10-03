from datetime import datetime as dt
import time

def time_calc (function):
    def calculate_time():
        now = time.time()
        function()
        later = time.time()

        elapsed = later-now

        print(elapsed)


    return calculate_time





@time_calc
def say_hello():
    time.sleep(4.5)
    print('hello')


say_hello()