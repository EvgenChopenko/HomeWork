sotki = int(input())*100# входные параметры перевод из соткок в м^2 1ар = 100m^2
k = 15*25# 15*25 m^2
#print (sotki,k)
if sotki == 0:
    print(0)
elif sotki < k:
    print (0)
elif sotki >= k:
    count = sotki-(sotki // k)*k
    print(count)# ответ в m^2



