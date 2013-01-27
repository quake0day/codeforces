n = map(int,raw_input().split())
table = []
[table.append(raw_input().split()) for i in xrange(n[0])]
for word in table:
    a = str(word)
    length = len(a) - 4
    if length > 10:
        print a[2]+str(length-2)+a[-3]
    else:
        print word[0]

