n, k = list(map(int,input().split()))

bill = list(map(int,input().split()))

charged = int(input())

bill.pop(k)

actual = sum(bill)/2

if charged==actual:
    print('Bon Appetit')

else:
    print(int(charged-actual))