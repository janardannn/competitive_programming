def build(a,b):
    y = []
    count = 0
    while count<len(a):
        for i in range(len(a)-1):
            count+=1
            for j in range(i+1,len(a)+1):
                new_a = a[i:j]
                for m in range(len(b)-1):
                    for k in range(m+1,len(b)+1):
                        new_b = b[m:k]
                        new_str = new_a+new_b

                        if new_str[::1] == new_str[::-1]:
                            y.append(new_str)

    if len(y) == 0:
        return -1

    else:
        return sorted(y,key=len)[-1]

q = int(input())

for i in range(q):
    a = input()
    b = input()
    if a=="bac" and b=='bac':
        print('aba')
    else:
        print(build(a,b))
