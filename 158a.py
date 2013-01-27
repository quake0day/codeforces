n,k = map(int,raw_input().split())
table = []
[table.append(raw_input().split())]
total = 0
for i in xrange(n):
    if ((int(table[0][i]) >= int(table[0][k-1])) and int(table[0][i]) != 0):
        total = total+1

print total
