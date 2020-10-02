t = int(input())

while t>0:
    n = int(input())
    markers = list(map(int,input().split()))
    edges = []
    for i in range(n-1):
        edges.append(list(map(int,input().split())))
    unatt = []
    for m in edges:
        if abs(m[0] - m[1]) == 1:
            unatt.append(abs(markers[m[0]-1] - markers[m[1]-1]))

    print(sorted(unatt)[0])
    t-=1