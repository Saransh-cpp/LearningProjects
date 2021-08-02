import time
import threading

def sleep_pls(s):
    print("Hello1")
    time.sleep(s)
    print("Hello2")

e = threading.Event()
p = threading.Thread(
    target=sleep_pls,
    args=(8,),
)

p.start()
# time-out
p.join(5)

if p.is_alive():  # pragma: no cover
    print("Alive")
    raise Exception("Alive")

    # e.set()

print("Bahar")