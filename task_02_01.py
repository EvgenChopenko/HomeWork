def is_palindrome(s):
    output = list()
    s=str(s)# преобразуем все входные параметры в строки
    s = s.strip(".")# удаляем точку в конце и в начале
    for w in s.split():
        output.append(w.strip(','))# удаляем пробелы в тексте и запятые
    s =(''.join([str(m) for m in output]))# преобразуем list в строку строка без пробелов
    s=s.lower()#все символы без регистра
    if s == s[::-1]:# если строка равна с реверсом то TRUE ибо False
        return True
    else:
        return False


