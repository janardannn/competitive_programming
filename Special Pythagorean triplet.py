from math import pow

for i in range(1,1000):
    for j in range(1,1000):
        for k in range(1,1000):
            if i+j+k==1000:
                if pow(k,2) + pow(j,2) == pow(i,2):
                    print(f'{k} + {j} = {i}')
                    print("-------------")
                    print(f'{k}^2 + {j}^2 = {i}^2')
                    product = i*j*k
                    print(f'product is {product}')
                    exit(1)