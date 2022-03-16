masalar = dict()
for i in range(10):
    masalar[i] =0

def hesapSil():
    masaNo = int(input("masa No :"))
    gecerli = masalar[masaNo]
    eksilecek = float(input("eksilecek ücret:"))
    toplam = gecerli - eksilecek
    if toplam < 0:
        print("işlemde hata var ")
    else:
        masalar[masaNo] = toplam

def kayitGuncelle():
    dosya = open("kayitlar.txt","r")
    for i in range(10):
        ucret=masalar[i]
        ucret=str(ucret)
        dosya.write(ucret + "\n")
    dosya.close()

def hesapKontrol(dosya_adi):

    try:
        dosya = open(dosya_adi)
        veriler = dosya.read()
        veriler = veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag=True
    except FileNotFoundError:
        dosya = open(dosya_adi,"w")
        dosya.close()
        print("ilk açılma")
        flag=False
    if flag:
        for i in enumerate(veriler):
            masalar[i[0]] = float(i[1])
    else:
        pass


def hesapEkle():
    masaNo = int(input("masa No :"))
    gecerli =masalar[masaNo]
    eklenecek= float(input("eklenecek ücret:"))
    toplam = gecerli + eklenecek
    masalar[masaNo]=toplam

def main():
    hesapKontrol("kayitlar.txt")

    while True:
        print("""
        1 masa görüntüle
        2 hesap ekle
        3 hesap sil
        q çıkış
    
    
        """)
        secim = input("işleminiz :")
        if secim =="1":
            for i in range(10):
                print("masa {} için hesap : {}".format(i,masalar[i]))
            print("işlem tamam enter bas")
            input()
        elif secim == "2":
            hesapEkle()
            print("işlem tamam enter bas")
            input()
        elif secim == "3":
            hesapSil()
            print("işlem tamam enter bas")
            input()
        elif secim =="q" or "Q":
            quit()
            kayitGuncelle()

main()