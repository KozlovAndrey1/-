import random as ra
N=int(input()) #Кол-во попыток
nuzn_komb=int(input()) #Нужная комбинация
print('Нужная комбинация: ', nuzn_komb)
blago=0
for i in range(N):
    a=ra.randint(1,6)
    b=ra.randint(1,6)
    c=ra.randint(1,6)
    print(a,b,c)
    if a+b+c==nuzn_komb:
        blago=blago+1
print('Благоприятные:',blago,' Всего:',N)
