n=int(input())
if n%2==0:
    q=n/2
else:
    q=(n-1)/2    
def fac(n):
 if n==0:
   return 1
 return fac(n-1)*n
c1=fac(n)/(6*fac(n-3))
c2=fac(q)/(6*fac(q-3))
p=c2/c1
print(p)
