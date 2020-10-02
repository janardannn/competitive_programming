import math

def list_to_string(li):

	string = ''
	for k in li:
		string += k

	length = len(string)

	rows = math.floor(math.sqrt(length))
	cols = math.ceil(math.sqrt(length))

	return string,rows,cols

def encryption(inp):

	string,row, column = list_to_string(inp)

	encryp = ''

	for i in range(row+1):
		k = i
		while k < len(string):
			encryp += string[k]
			k += column
		encryp += ' '

	return encryp


def main():
	inp = list(input().split())
	print(encryption(inp))

main()