import random as ra
N=int(input()) #Кол-во попыток
blago=0
print('кол-во попыток: ',N)
for i in range(N):
 avt_vr=[]
 avt_pr=ra.randint(0,60)
 avt_1=avt_pr
 for i in range(5):
     avt_vr.append(avt_1)
     avt_1=avt_1+1
 print('Время ожидания авто: ',avt_vr)
 ch_vr=[]
 ch_pr=ra.randint(0,60)
 ch_1=ch_pr
 for i in range(10):
     ch_vr.append(ch_1)
     ch_1=ch_1+1
 print('Время ожидания человека:',ch_vr)
 result=list(set(avt_vr) & set(ch_vr))
 print(result)
 if result!=[]:
     blago=blago+1
print('Кол-во благоприятных: ',blago)
    
