n = int(input())

nums = list(map(int,input().split()))

for i in nums:
    if len([k for k in range(1,i+1) if i%k==0]) == 3:
        print('YES')

    else:
        print('NO')