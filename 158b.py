n = map(int,raw_input().split())[0]
table = []
[table.append(raw_input().split())]
total = 0
group3 = 0
group2 = 0
group1 = 0
group4 = 0
for i in xrange(n):
    if (int(table[0][i]) == 4):
        group4 = group4 + 1
    if (int(table[0][i]) == 3):
        group3 = group3 + 1
    if (int(table[0][i]) == 1):
        group1 = group1 + 1
    if (int(table[0][i]) == 2):
        group2 = group2 + 1

group1left = group1 - group3
if group1left < 0:
    group1left = 0
total =  group4 + group3 
group2c = group2 / 2
if group2c > 0:
    total = total + group2c
group2m = group2 % 2
if group2m != 0:
    if group1left != 0:
        total = total + 1
        group1left = group1left -2
        if group1left < 0:
            group1left = 0
    else:
        total = total+1
        group1left = group1left -2
        if group1left < 0:
            group1left = 0

if group1left > 0:
    total = total + (group1left+3) / 4
    

print total
