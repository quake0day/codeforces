p = map(int,raw_input().split())[0]
k = 0
i = 0
while (p - k * 5) > 0:
    p = p - k * 5
    k = 2**i
    i = i + 1
if i-1 > 0:
    ans = (p+2**(i-1)-1) / 2** (i-1)
else:
    ans = p

List = ["Sheldon","Leonard","Penny","Rajesh","Howard"]
print List[ans-1]
