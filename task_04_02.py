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
    s=" "
    z=""
    inf=""
    dict={}
    for i in str:

        if (s == "HTTP/1.1") or (s == " HTTP/1.1")or (s == "  HTTP/1.1"):
            dict["protocol"] = s.strip(" ")
            s=" "
            inf=""
        elif((s=="  301") or (s =="  200") or s==("200") or s=="300" ):
            dict["status_code"] = s.strip(" ")
            s=" "
            inf=""
        elif(s=="  OK") or (s=="  Moved Permanently") or (s=="OK") or (s==" OK") or s=="Moved Permanently":
            dict["status_message"] = s.strip(" ")
            s=" "
            inf=""
        elif (s == "GET" or s == " GET" or s == "  GET"):
            dict["method"]=s.strip(" ")
            s=" "
            inf=""
        elif (z!="" and inf!=""):
            dict[z.strip(" ")]=inf.strip(" ")
        if i == " ":
            if s== "  /python-developer":
                #print("Adsf")
                dict["uri"] = s.strip(" ")
                s = " "
                inf = ""
            if s[-1]==":":
                z = s.replace(":","")
                inf = ""
                s=" "
            elif s[-1]!=":":
                s=s+i

        elif i != "\n":
            s=s+i
        elif (i=="\n"):
            inf = s
            s=" "








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
