import time
import random

x = 0
def func():
    print(f"Hashrate: {random.randint(10, 100)}. Usama is happy!")
    global x
    x = 0

while x < 15:
    print(f"Share accepted! {random.randint(10,20)}G")
    time.sleep(0.5)
    x = x+1
    if x == 15:
        func()
