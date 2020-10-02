word = 'hello'

he_type = ''

s = input().strip()

k = 0

for i in s:
    if i == word[k]:
        he_type += i
        k+=1
        if k==len(word):
            break

if he_type == word:
    print('YES')

else:
    print('NO')
