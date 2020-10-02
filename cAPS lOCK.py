word = str(input().strip())

if len(word)==1:
    if word.islower():
        print(word.upper())
    elif word.isupper():
        print(word.lower())
elif word[0].islower() and word[1::].isupper():
    word=word[0].upper()+word[1::].lower()
    print(word)
elif word.isupper():
    print(word.lower())
else:
    print(word)