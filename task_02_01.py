def is_palindrome(s):
    output = list()
    s=str(s)# преобразуем все входные параметры в строки
    for w in s.split():
        output.append(w)# удаляем пробелы в тексте
    s =(''.join([str(m) for m in output]))# преобразуем list в строку строка без пробелов
    s=s.lower()#все символы без регистра
    if s == s[::-1]:# если строка равна с реверсом то TRUE ибо False
        return True
    else:
        return False