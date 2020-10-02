# codeforces question
# googol string

import math

def switch(x):
    new_string = ""
    for i in x:
        if i == "0":
            new_string += "1"
        elif i =="1":
            new_string += "0"
    return new_string

def reverse(x):
    new_string = x[::-1]
    return new_string

def googol_sentence (x):
    line = ""
    prev_line = "0"
    new_line = ""
    if x > 3:
        for i in range(3,x+2):
            new_line = prev_line + "0" +switch(reverse(prev_line))
            line = prev_line
            prev_line = new_line
        return new_line
    if x<=3:
        if x==3:
            return "0010011"
        elif x==2:
            return "001"
        elif x==1:
            return "0"
        elif x ==0:
            return ""

t = int(input())
if t < 1 or t >100:
    exit()

k_values = []
for i in range(t):
    j = int(input())
    k_values.append(j)
num = 1

for j in k_values:
    case = googol_sentence(j)
    print("Case #{}: {}".format(num,case[j-1]))
    num+=1


