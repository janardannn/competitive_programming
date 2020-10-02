n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))

if sorted(p,reverse=True)[0] == n and sorted(q,reverse=True)[0] == n:
    print('Oh, my keyboard!')

elif sorted(p,reverse=True)[0] >= n or sorted(q,reverse=True)[0] >= n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')