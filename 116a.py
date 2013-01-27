n = map(int,raw_input().split())[0]
table = []
[table.append(raw_input().split()) for x in xrange(n)]
total = 0
max = 0
#print table
for i in table:
    #print i[0]
    #print i[1]
    total = total - int(i[0]) + int(i[1])
    if total > max:
        max = total
print max
