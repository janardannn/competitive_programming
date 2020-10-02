def prime(x):
    primes = []

    for i in range(2,x+1):
        flag = 1
        for k in range(1,i):
            if k==1:
                continue
            elif k==i:
                continue
            elif i%k==0:
                flag = 0
        if flag==1:
            primes.append(i)
    return primes

prime_list = prime(10000)

su = 0

for k in prime_list:
    su += k
    if su < 10000:
        print(su)