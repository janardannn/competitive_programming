def choose(mercenaries,pairs):

	count = 0

	for k in mercenaries:
		chosen = 0
		sub_count = 0
		if chosen+1 >= k[0] and chosen <= k[1]:
			count += 1

			mx = k[1]
			if chosen+1 < mx:
				for kk in range(len(mercenaries)*3):
					for i in mercenaries:
						if i!=k and chosen+1 < i[1]:
							if [mercenaries.index(k)+1,mercenaries.index(i)+1] not in pairs and [mercenaries.index(i)+1,mercenaries.index(k)+1] not in pairs:
								chosen += 1
						
				if chosen != 0:
					count += 1	

	return (count)

n,m = list(map(int,input().split()))

mnaries = []
hate_pairs = []

for k in range(n):

	mnaries.append(list(map(int,input().split())))

for k in range(m):

	hate_pairs.append(list(map(int,input().split())))

print(choose(mnaries,hate_pairs))