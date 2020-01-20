import time

def hello(n):
    for i in range(n):
        print(i+1, "번째 : hello")

# hello(3)

def evenodd(n):
    if n %2 ==0:
        print("even")
    else:
        print("odd")

# evenodd(int(input("n: ")))

def square():
    i=1
    while (i<2 ** 32):
        print(i)
        i *= 2
        time.sleep(0.5)

# square()

