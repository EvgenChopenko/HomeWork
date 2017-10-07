import os
import json
def read_data(name):# функция считывает файл если файла нет то возвращает none
    if(os.path.exists(name)):
        with open(name) as file:
            data = file.read()
            return data
    else:
        return None


#__________________________________________________________________________

def to_DICT(str):# парс файла  и формирования его в словарь.
    s=""
    z=" "
    inf=""
    dict={}
    #print(str)
    str=str.replace("\n","~")# переход на следушию строку замене ~
    str = str.replace(" ", "#")# пробел на #
    #print(str)
    for i in str:
        if i != "#":
            s=s+i
            if z[-1]==":":
                inf = inf+i
                s=""
            elif(z[-1]!=":"):
                z = s
            if (i =="~") and (inf != ""):
                dict[z.strip(":")] = inf.strip("~")
                z = " "
                inf = ""
                s = ""
            if(s == "OK~") or (s=="Moved") :# ключевые слова возможно дополнения
                dict["status_message"] = s.strip("~")
                s = ""
                inf = ""
            if (s == "Permanently~"):# игнор данных в файле
                s = ""
                inf = ""
            if (s == "HTTP/1.1~"):
                dict["protocol"] = s.strip("~")
                s = ""
                inf = ""
        elif i == "#":
            if (s =="HTTP/1.1"):
                dict["protocol"]=s
                s=""
                inf=""
            elif(s=="301") or s=="200":
                dict["status_code"]=s
                s=""
                inf=""
            elif (s=="GET"):
                dict["method"]=s
                s=""
                inf=""
            if (s == "Permanently~"):# игнор данных в файле
                s = ""
                inf = ""
            elif (s=="ОК")or(s=="Moved"):
                dict["status_message"]=s
                s=""
                inf=""
            elif (z[0] == "/"):
                dict["uri"] = s
                s = ""
                inf = ""
    return dict
#_________________________________________________________________________________________
def writeToJSON(name,DICT):#запись JSON
    with open(name,"w") as file:
        json.dump(DICT,file,indent=4)
#_____________________________________________________________________________________________


def http_headers_to_json(file_in_html,file_out_json):# основная функция
    Dict={}
    Dict=to_DICT(read_data(file_in_html))
    writeToJSON(name=file_out_json,DICT=Dict)




#________проверка ______________________________________________

if(__name__=="__main__"):
    http_headers_to_json("headers-1.txt","result-1.json")
    http_headers_to_json("headers-2.txt", "result-2.json")
    http_headers_to_json("headers-3.txt", "result-3.json")
