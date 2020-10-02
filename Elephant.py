x = int(input())
h = 0
steps = 1

while True:
    h+=1
    if h%5==0 and h<x:
        steps+=1
    elif h==x:
        print(steps)
        break