def test(arr):
	ne_arr = []
	for i in arr:
		n = 0
		if i < 0:
			n = i
			arr.pop(arr.index(i))
			ne_arr.append(n)

	arr = sorted(arr)
	ne_arr = sorted(ne_arr,reverse=True)
	
	m = arr+ne_arr
	for i in m:
		print(i,end=" ")

	print("\n")

t = int(input())

for i in range(t):
	n = int(input())
	a = list(map(int,input().split()))

	test(a)