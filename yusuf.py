kutuphane = ["kitap", "makale", "deneme"]

def cikar():
    x = input("Çıkarmak istediğiniz kitabın adını giriniz :")
    y = input("Yazarın adını giriniz :")
    z = input("Sayfa sayısını giriniz :")
    v = x + "-" + y + "-" + z + "\n"

    if v in kutuphane:
        kutuphane.remove(v)

        with open("saves.txt", "a") as saves:
            saves.write(kutuphane)
            print("{} başarıyla kaldırıldı".format(v))

    else:
        print("Böyle bir kitap yok !")

cikar()