def check_row_sum(square):

	if sum(square[0]) == sum(square[1]) == sum(square[2]):
		return True

	elif sum(square[0]) == sum(square[1]) != sum(square[2]):
		return 3

	elif sum(square[0]) == sum(square[2]) != sum(square[1]):
		return 2

	elif sum(square[2]) == sum(square[1]) != sum(square[0]):
		return 1
  
def change_row_values(square):

	ret = check_row_sum(square)
	
	if ret:
		return True
	elif ret == 1:
		for k in range(3)


sq = []

for k in range(3):
	row = sq.append(list(map(int, input().split())))

turn_into_magic_square(sq)