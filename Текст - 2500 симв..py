import random as ra
print('Кол-во повторов программы: ')
N=int(input()) #Кол-во прогонов программы
opech=0 #Кол-во опечаток
n=[] #Кол-во благопр. соб.
spis=[]
for i in range(0,N):
 for j in range(0,2500):
     a=ra.random()
     if a<=0.001:
         opech=opech+1
         spis.append(opech)
 k=len(spis)
 if k<2:
     n.append(1)
 spis=[]
print('Благоприятные события: ',len(n))
 
