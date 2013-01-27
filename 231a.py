n = map(int,raw_input().split())[0]
table = []
[table.append(raw_input().split()) for x in xrange(n)]
total = 0
for ele in table:
    sure = 0
    for k in ele:
        sure = sure + int(k)
        if sure >=2:
            total = total + 1
            break
print total
