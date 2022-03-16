# sayi = float(input("sayı: "))
# if 0 < sayi < 100:
#     print("sayı 0-100 aralığındadır.")
# else:
#     print("sayı 0-100 aralığında değildir.")    

# sayi = float(input("sayı: "))
# if (sayi > 0):
#     if (sayi % 2 == 0):
#         print("sayı pozitif ve çifttir.")
#     else :
#         print("sayı pozitif ama çift değildir.")
# else:
#     print("sayı negatiftir.")


# email = "enes@gmail.com"
# password = "123123"
# girilenMail = input("email: ")
# girilenPassword = input("parola: ")
# if (email == girilenMail):
#     if (password == girilenPassword):
#         print("GİRİŞ BAŞARILI")
#     else:
#         print("parola hatalı")
# else:
#     print("mail hatalı")

# a = int(input("1.sayı: "))
# b = int(input("2.sayı: "))
# c = int(input("3.sayı: "))
# if a<b<c:
#     print("{a} < {b} < {c} ")
# elif 

# vize1 = float(input("1. vize: "))
# vize2 = float(input("2. vize: "))
# final = float(input("final: "))
# ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)
# gerekli = (final>=50 and (ortalama>=50 or final>=70))
# if final>=50:
#     if (ortalama>=50 or final>=70):
#         print(f"{ortalama} ortalamayla sınıfı geçtiniz.")
#     else:
#         print(f"ortalamanız( {ortalama} ) 50'den düşük olduğundan ya da final notunuz 70'den düşük olduğundan kadlınız.")
# else:
#     print(f"final 50'den düşük olduğu için {ortalama} ortalamayla kaldınız.")


isim = input("isminiz: ")
kilo = float(input("kilonuz: "))
boy = float(input("boyunuz: "))
formul = ((kilo) / (boy ** 2))
if 0 <= formul <= 18.49:
    print(f"indexiniz {formul} ve kategoriniz : zayıf")
elif 18.5 <= formul <= 24.99:
    print(f"indexiniz {formul} ve kategoriniz : normal")
elif 25 <= formul <= 29.99:
    print(f"indexiniz {formul} ve kategoriniz : kilolu")
else:
    print(f"indexiniz {formul} ve kategoriniz : obez")