n = int(input())

p = int(input())

fw_page = 0

if p == 1:
	print("0")
	exit()

elif p == n:
	print("0")
	exit()

m = 0
while m==0:
	for i in range(2,n):
		for j in range(i,i+2):
			if p == j:
				fw_page = i/2
				m=1

l = n-1
pages = []

m = 0
if n%2==0:
	bw_page = 1
	while m==0:
		pages = [l,l-1]
		if p in pages:
			m=1
		else:
			l-=2
			bw_page+=1

elif n%2!=0:
	m = 0
	bw_page = 0
	while m==0:
		pages=[n,n-1]
		if p in pages:
			m=1
		else:
			n-=2
			bw_page+=1

if bw_page<fw_page:
	print(int(bw_page))
elif bw_page==fw_page:
	print(int(fw_page))
else:
	print(int(fw_page))