a,b,n = map(int,raw_input().split())
def gcd(k,n):
    if k ==0 or n == 0:
        return n+k
    else:
        return gcd(n,k%n)
i = 1
while n != 0:
    if i % 2  == 1:
        n = n - gcd(a,n)
        i= i+1
    else:
        n = n - gcd(b,n)
        i= i +1
    #print n
print i%2


    
