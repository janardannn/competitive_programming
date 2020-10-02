n = input()
s = list(map(int,input().split()))
mn = s[0]
mn_c = 0
mx = s[0]
mx_c = 0

for i in s:
    if i<mn:
        mn = i
        mn_c += 1
    elif i>mx:
        mx = i
        mx_c += 1

print(str(mx_c) + " " + str(mn_c))
