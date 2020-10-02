#def next_move(n,r,c,grid):


n = int(input())
if n>99:
    exit()

r,c = list(map(int,input().split()))

grid = []

for i in range(n):
    grid.append(list(input()))

print(grid)