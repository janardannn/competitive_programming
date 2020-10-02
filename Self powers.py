from math import pow

s = 0

for i in range(1,1001):
    s += i**i

lasts = []

temp = s

for i in range(10):
    last = temp%10
    lasts.append(last)
    temp //= 10
    temp = int(temp)

st = ""
for k in lasts:
    st+=str(k)

print(st)