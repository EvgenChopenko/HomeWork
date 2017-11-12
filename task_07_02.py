import random


def password_generator(n):
    str1= "0123456789"
    str2= "qwertyuiop[]asdfghjkl;'zxcvbnm,./!@#$%^&*()_+-=?><{}:|\/"
    str3=str2.upper()
    str3=str3+str2+str(str1)
    return (random.choice(str3) for i in range(n))


if (__name__=="__main__"):
    print (password_generator(16))