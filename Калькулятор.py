while True:
 a=float(input())
 g=input()
 b=float(input())
 result= None

 if (g) =='+':
     result=a+b
     print('Result: ',result)
 elif (g) =='-':
     result=a-b
     print('Result: ',result)
 elif (g) =='*':
     result=a*b
     print('Result: ',result)
 elif (g) =='/' and b!=0:
    result=a/b
    print('Result: ',result)
 elif (g) =='/' and b==0:
     print('Error');
 
 elif (g) =='^':
  def res(a,b):
    if b==0:
        return 1
    elif b>0 and b==a:
        return a**b
    elif b>0:
        return a**b
    elif b<0:
        return ('Error')
  print('Result: ',res(a,b))
  
 elif (g)=='&':
     while a!=0 and b!=0:
         if a>b:
             a=a%b
         else:
             b=b%a
     result=a+b
     print('Result: ',result)
     
 elif (g)=='@' and b==0.5:
     print(a**b)
     
             
     
