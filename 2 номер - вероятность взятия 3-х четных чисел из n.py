import math as g
v=int(input())
p=None #общая вероятность
q=None #кол-во четных чисел
b=3
s=6*(g.factorial(v-b))
c1=g.factorial(v)/s #всего расстановок
if v//2:
    q=v/2
else:
    q=(v-1)/2
c2=g.factorial(q)/(6*(g.factorial(q-b))) #расстановок четных чисел
p=c2/c1
print(p)




