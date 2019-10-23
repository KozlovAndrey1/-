import random as ra

print('Банк первого:')
m=int(input())
s=m
print('Банк второго:')
n=int(input())
k=n

blago=0
proigr=0

if m==0:
    print('ПОБЕДА ВТОРОГО - ПЕРВЫЙ БЕЗ ДЕНЕГ')
if n==0:
    print('ПОБЕДА ПЕРВОГО - ВТОРОЙ БЕЗ ДЕНЕГ')

while m>0 and n>0:
    p1=ra.random() #Вер-сть победы в одном раунде первого (m)
    p2=1-p1 #Вер-сть победы в одом раунде второго второго (n)
    print('P1=',p1,'\nP2=',p2)
    if p1>p2:
        m=m+1
        blago=blago+1
    elif p2>p1:
        n=n+1
        proigr=proigr+1
    m=m-1
    n=n-1
    print('деньги после раунда(с учетом след.ставки):\n1ого:',m,'\n2ого:',n)

print('Деньги первого:',m,'\nДеньги второго:',n)

if m>n:
    print('\nПобеда Первого, его выигрыш=',s+k)
else:
    print('\nПобеда Второго, его выигрыш=',k+s)

vsego=blago+proigr
otv=blago/vsego
print('Вер-сть победы 1ого:',otv)

