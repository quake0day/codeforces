string1 = map(str,raw_input().split())[0]
string2 = map(str,raw_input().split())[0]

if string1.upper() == string2.upper():
    print 0
else:
    print cmp(string1.upper(),string2.upper())
