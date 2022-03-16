# sayı = int(input("sayı: "))
# sayı = (sayı < 100) and (sayı > 0)
# print(sayı)

# sayı = (sayı > 0) and (sayı % 2 == 0)
# print(sayı)


# kayıt1 = input("email kayıt: ")
# kayıt2 = input("parola kayıt: ")
# a = input("giriş email: ")
# b = input("giriş parola: ")
# basarı = (a == kayıt1) and (b == kayıt2)
# print(f"giriş durumu : {basarı}")

# a = float(input("1.sayı: "))
# b = float(input("2.sayı: "))
# c = float(input("3.sayı: "))

# vize1 = float(input("1. vize notu: "))
# vize2 = float(input("2. vize notu: "))
# final = float(input("final notu: "))
# ortalama = ((vize1 + vize2) / 2) * 0.6 + (final) * 0.4
# durum = ((50 <= ortalama) or (final >= 70)) and (final >= 50)
# print(f"bu dönemki not ortalamanız  {ortalama} ve sınıf geçme durumunuz : {durum}")


ad = (input("isim: "))
boy = float(input("boy: "))
kılo = float(input("kilo: "))
formul = (kılo / boy ** 2)
zayıf = (0 < formul < 18.4) 
normal = (18.5 < formul < 24.9)
fazlakılo = (25 < formul < 29.9)
obez = (30 < formul < 34.9)
print(f"vücut indeksiniz {formul} ve indeks grubunuz zayıf: {zayıf}")
print(f"vücut indeksiniz {formul} ve indeks grubunuz normal: {normal}")
print(f"vücut indeksiniz {formul} ve indeks grubunuz fazla kilolu: {fazlakılo}")
print(f"vücut indeksiniz {formul} ve indeks grubunuz obez: {obez}")