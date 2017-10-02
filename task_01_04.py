import math
l = list()

while l.__len__() < 6:
    l.append(int(input()))


x12= l[0]-l[2]
y12= l[1]-l[3]

x23=l[2]-l[4]
y23= l[3]-l[5]

x31=l[4]-l[0]
y31=l[5]-l[1]


a=((x12*x12) +(y12*y12))**0.5
b=((x23*x23) +(y23*y23))**0.5
c=((x31*x31) +(y31*y31))**0.5
#print (a,b,c)
if (c == (a*a + b*b)**0.5) or (a == (c*c+b*b)**0.5) or (b == (c*c + a*a)**0.5):
    print("Прямоугольный")
else:
    print("Не прямоугольный")
