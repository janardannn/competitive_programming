n,k = list(map(int,input().split()))

ar = list(map(int,input().split()))

pair = 0

for i in range(len(ar)):
    if i == len(ar)-1:
        continue
    for j in range(i+1,len(ar)):
        if i < j:
            if (ar[i] + ar[j])%k==0:
                pair +=1
        

print(pair)