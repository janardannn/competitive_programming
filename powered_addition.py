def time(arr):
	count = 0
	new_arr = arr
	for i in range(len(arr)):
		if i == len(arr)-1:
			pass
		elif new_arr[i] > new_arr[i+1]:
			count+=1
			while new_arr[i]>new_arr[i+1]:
				new_arr[i+1]+=1
	return count

t = int(input())

secs = []

for i in range(t):
	n = int(input())
	a = list(map(int, input().split()))
	secs.append(time(a))

for i in secs:
	print(i)