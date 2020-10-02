n = int(input())
leaderboard = list(map(int,input().split()))
m = int(input())
scores = list(map(int,input().split()))

data = {}
temp = 1
data[leaderboard[0]] = temp
for i in range(1,len(leaderboard)):
    if leaderboard[i] not in data:
        temp += 1
        data[leaderboard[i]] = temp

for score in scores:
    for z in data:
        if z <= score:
            print(data[z])
            break
        elif z == leaderboard[-1]:
            last = data[leaderboard[-1]]+1
            print(last)
            break 