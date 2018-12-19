import random as r
print('Кол-во элементов:')
N=int(input())
L=[round(r.uniform(0,N)) for i in range(N)]
L.sort()
L.reverse()
L1=L
N1=N*0.1
N1=round(N1)
for i in range(N-N1):
 L1=L[0:N-1]
 N=N-1
print(L1)
