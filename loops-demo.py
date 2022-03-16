import random
sayi = random.randint(1,10)

sayac = 0
can = int(input("kaç hakkınız olsun?: "))
hak = can
while hak>0:

    hak -= 1
    sayac += 1
    tahmin = int(input("tahmin: "))
    puan = 100-((100/can) * (sayac-1))

    if sayi == tahmin:
        print(f"tebrikler {sayac}. defada bildiniz. puanınız: {puan} ")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if hak == 0:
        print(f"hakkınız bitti. tutulan sayı {sayi} ")
