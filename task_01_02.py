Ndishes = int(input())# колво тарелок
Nfairy = int(input())# кол-во моющего
k = 1 / 2  # коэфициент затрат
if (Ndishes != 0 and Nfairy !=0):
    n = 0  # кол-во вымытых тарелок
    N = Ndishes  # остаток грязных тарелок Ndished -n
    nfairy = 0  # расход моющего
    i=0 # счетчик
    while True:
        if nfairy == Nfairy and  N!=0:
            print("Моющее средство закончилось. Осталось {} тарелок".format(N))
            break
        elif N == 0 and nfairy != Nfairy:
            print("Все тарелки вымыты. Осталось {} ед. моющего средства".format(Nfairy - nfairy))

            break
        elif nfairy == Nfairy and N == 0:
            print("Все тарелки вымыты, моющее средство закончилось")
            break
        n = n+ 1
        nfairy =  n * k
        N = Ndishes - n
elif (Nfairy==0 and Ndishes !=0 ):
    print("Моющее средство закончилось. Осталось {} тарелок".format(Ndishes))
elif (Nfairy != 0 and Ndishes == 0):
    print("Все тарелки вымыты. Осталось {} ед. моющего средства".format(Nfairy))
else:
    print("Все тарелки вымыты, моющее средство закончилось")