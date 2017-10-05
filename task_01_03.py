lst = list()
while lst.__len__() < 3:
    lst.append(int(input()))
n=1
i=0
while n < len(lst):
    for i in range(len(lst) - n):
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            #print(i)
    n += 1

s= ','.join([str(m) for m in lst])
s=s.replace(" ","")
print(s)# ужасный способ вывода ((
