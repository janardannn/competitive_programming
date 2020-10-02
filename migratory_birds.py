n = input()
birds = list(map(int,input().split()))
print(max(birds,key=birds.count))