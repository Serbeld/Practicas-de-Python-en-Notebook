# Serie de Fibonacci
import time

a, b = 0, 1

while (b <= 10000):
    a = b + a
    print(b)
    time.sleep(1)
    print(a)
    time.sleep(1)
    b = a + b
time.sleep(1)
print("End\n")
