def func(x,y):
	count = 0
	for i in x:
		c = 0
		for j in y:
			if j%i==0:
				c+=1
			else:
				0
		if c==len(y):
			count += 1
	return count

m,n = list(map(int,input().split()))

a = list(map(int,input().split()))
b = list(map(int,input().split()))

h = b[-1]

possible = []
count  = 0



for i in range(1,h+1):
	c = 0
	while c < len(a):
		if i % a[c] == 0:
			c+=1
		else:
			break
	if c == len(a):
		possible.append(i)

print(func(possible,b))
