lst = list()
while lst.__len__() < 3:
    lst.append(int(input()))

# метод пузырька
n=lst.__len__()-1

i=0# первый элемент
j=1# i+1
a=None# промежуточный коэфициент для сортировки
while i <n:
    while j<n+1:
        if lst[i]>lst[j]:
            a=lst[j]
            lst[j]=lst[i]
            lst[i]=a
        j=j+1
        i=i+1
i=0
j=1
while i <n:
    while j<n+1:
        if lst[n-i]<lst[n-j]:
            a=lst[n-j]
            lst[n-j]=lst[n-i]
            lst[n-i]=a
        j=j+1
        i=i+1


    print(','.join([str(m) for m in lst]))# ужасный способ вывода ((
