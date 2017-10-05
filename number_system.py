def convert(str):# доп функция нужня для функции dectodigital , для замены 10 в А , 11 в В........
    DICT = {'10': 'a',
            '11': 'b',
            '12': 'c',
            '13': 'd',
            '14': 'e',
            '15': 'f'
            }
    if DICT.get(str) !=None:
        return DICT.get(str).upper()
    else:
        return str

def str_type(st):# доп функция для удаления избыточных символов
    DICT = {ord(' '): '',
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
#-------------------------------------------------------------------------------------------------------------------
def bintodigit(digit_num):# digit_num разрядность системы / number строка 0101; 0..7; 0...F
    def binto(number):#функция преобразует строку с кодом bin, oct, hex в int
        DICT = {ord('a'): '10',
                ord('b'): '11',
                ord('c'): '12',
                ord('d'): '13',
                ord('e'): '14',
                ord('f'): '15'
               }
        number=str(number).lower()
        list = number[::-1]
        i = 0
        num = 0
        while i < list.__len__():
            num = num + (int(list[i].translate(DICT)) * (digit_num ** i))
            i += 1
        return int(num)
    return binto
#------------------------------------------------------------------------------------------------------------
def dectodigital(digit_num):# функция преобразвет любое 10 число в формат digit_num: (2,8,16)-разрядность
    def decto(number):
        s = list()
        if number == 0:
           return str(0)
        else:
            while (number) >0 :
                s.append(convert(str(number % digit_num)))
                number = (number // digit_num)
            s=s[::-1]
        return str("".join([str(i) for i in s]))
    return decto
#--------------------------------------------------------------------------------------------------------------
def dec2bin(number):#return str
    if(type(number)==int):
           s=dectodigital(2)
           return s(number)
    else:
        return None

def dec2oct(number):#return str
    if (type(number) == int):
        s = dectodigital(8)
        return s(number)
    else:
        return None
def dec2hex(number):#return str
    if (type(number) == int):
        s = dectodigital(16)
        return s(number)
    else:
        return None
#------------------------------------------------------------------------------------------------------------
def  bin2dec(number):#return int
    number=str_type(number)
    s=bintodigit(2)
    return s(number)

def oct2dec(number):#return int
    number = str_type(number)
    s = bintodigit(8)
    return s(number)

def hex2dec(number):#return int
    number = str_type(number)
    s = bintodigit(16)
    return s(number)
#___________________________________________________________________________

# проверка
if (__name__=="__main__"):
    print("bin to dec:",bin2dec("10100<11010"))
    print("oct_to_dec:",oct2dec("755"))
    print("hex to_dec:",hex2dec("ABCDEF."))
    print("dec To bin:",dec2bin(250))
    print("dec To oct:",dec2oct(250))
    print("dec To 16:", dec2hex(250))
    print(convert("9"))
    print(str_type("ABV,.LL      "))

# атрибут
__all__ = [
    'bin2dec',
    'oct2dec',
    'hex2dec',
    'dec2bin',
    'dec2oct',
    'dec2hex'
]

