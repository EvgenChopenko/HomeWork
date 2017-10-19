def fibonacci(n):
   a= 0
   b=1
   s=[]
   for i in range(n):
       a,b = b, a + b
       s.append(a)
   return ' '.join(str(i) for i in s)





if(__name__=="__main__"):
    print(fibonacci(10))

