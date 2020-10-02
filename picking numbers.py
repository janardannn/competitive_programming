def func(x,ar):
	sub = []
	for k in ar:
		if abs(x-k)<=1:
			sub.append(k)

	return len(sub)-1

n = int(input())
arr = list(map(int,input().rstrip().split()))
total = []
done = []
for k in arr:
	if k not in done:
		total.append(func(k,arr))
print(max(total))