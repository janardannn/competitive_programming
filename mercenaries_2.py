def choose(mercenaries,pairs):

	count = 0

	subsets = []

	for k in mercenaries:
		chosen = 0
		if chosen+1 >= k[0] and chosen <= k[1]:
			subsets.append(k)

			mx = k[1]
			if chosen+1 < mx:
					for i in mercenaries:
						if i!=k and chosen+1 >= i[0] and chosen+1 < i[1]:
							if [mercenaries.index(k)+1,mercenaries.index(i)+1] not in pairs and [mercenaries.index(i)+1,mercenaries.index(k)+1] not in pairs:
								chosen += 1
								subsets.append(i)

	print(subsets)
	return (len(subsets))

n,m = list(map(int,input().split()))

mnaries = []
hate_pairs = []

for k in range(n):

	mnaries.append(list(map(int,input().split())))

for k in range(m):

	hate_pairs.append(list(map(int,input().split())))

print(choose(mnaries,hate_pairs))