flag = 1

longest = 0

record = ''

for k in range(2,1000000):
	chain = ''
	num = k

	while True:
		chain+=str(k)
		if k%2==0:
			chain+="->"
			k = int(k/2)

		elif k==1:
			break

		elif k%2!=0:
			chain+='->'
			k = int((3*k) + 1)

	temp = len(chain)

	if temp>longest:
		longest=temp
		record ="length: " +str(longest) + " " +'number: '+ str(num)

print(record)

