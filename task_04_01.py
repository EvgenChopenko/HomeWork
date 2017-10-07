import os# необходима для проверки наличия файла
n=int(input())
p=int(input())
#------------------------------------------------------------------------
def str_type(st):# доп функция для удаления избыточных символов
    DICT = {
            ord('.'): '',
            ord(','): '',
            ord('!'): '',
            ord('?'): '',
            ord(':'): '',
            ord(';'): '',
            ord('#'): '',
            ord('*'): '',
            ord('<'): '',
            ord('>'): ''}
    s=list(str(st).translate(DICT))
    return str(str("".join([str(i) for i in s])))
#_________________________________________________________________________
def read_data():# функция считывает файл если файла нет то возвращает none
    if(os.path.exists('data.txt')):
        with open('data.txt') as file:
            data = file.read()
            return data
    else:
        return None

#_____________________________________________________________________
def strTOint_list(s):# функция преобразуте строку с числами в список int,  разделитель между числами пробел. Защиат от лишних пробелом и символов набора.
   if s == None:
       return None
   else:
    s = str_type(s)
    str=""
    data_list = list()
    for i in s:
        if i!=" ":
            str=str+i
        elif i==" " and str!="":
            try:
                data_list.append(int(str))
            except BaseException:
                data_list.append(0)
            str=""
        elif i==" " and str=="":
            str=""
    data_list.append(int(str))
    return(data_list)# если будет не допустимый символ "буква" то будет нул
#________________________________________________________________________
def datadelto(n,list):# деление без остатка list // n возврашает тольке те котороые без остатка
    l=[]
    for i in list:
        if i%n ==0:
           l.append((i))
    return l

def data2to(p,list):#возводит значения list  в степень **p
    l = []
    for i in list:
        l.append(i**p)
    return l


#_____________________________________________________________________________

def write_list(list,name):
    with open(name,"w") as file:
        for i in list:
            file.write(str(i))
            file.write(" ")




# проверка _______________________________________________

if(__name__=="__main__"):
  s= strTOint_list(read_data())
  d=data2to(p, s)
  dele=datadelto(n,s)
  print(d)
  print(dele)
#_______________________________________________________________________
# реализация


s= strTOint_list(read_data())
d=data2to(p, s)
dele=datadelto(n,s)
write_list(name="out-2.txt",list=d)
write_list(name="out-1.txt", list=dele)