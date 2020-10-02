c_b,o = list(map(int,input().split()))

rq,cq = list(map(int,input().split()))
rq -=1
cq-= 1

obstacles = []
for i in range(o):
    s = list(map(int,input().split()))
    obstacles.append(s)

obs = []
for i in obstacles:
    s= []
    for j in i:
        j-=1
        s.append(j)
    obs.append(s)

chessboard=[]
for i in range(1,c_b+1):
    sub_board = []
    for j in range(1,c_b+1):
        s = list([i,j])
        sub_board.append(s)
    chessboard.append(sub_board)
    sub_board = []

points = 0

for j in range(rq):
    for m in obs:
        if chessboard[j][cq] == m:
            points = 0
        else:
            points += 1
flag = 0
while flag==0:
    for j in range(rq+1,len(chessboard)):
        for m in obs:
            if chessboard[j][cq] == m:
                flag=1
                break
            else:
                points+=1
    if j==len(chessboard)-1:
        flag=1

print(points)





'''
5 2
3 2
1 2
4 2

'''