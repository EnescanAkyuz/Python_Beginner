# ad = input("isminiz: ")
# yas = int(input("yaşınız: "))
# egitim = input("eğitim düzeyi: ")

# if yas >= 18: 
#     if egitim == "lise" or egitim == "üniversite":
#         print("ehliyet için uygun")
#     else:
#         print("ehliyet için yetersiz.eğitim yetersiz.")
# else:
#     print("ehiiyet için yetersiz.yaş tutmuyor.")


# yazılı1 = float(input("1. yazılı: "))
# yazılı2 = float(input("2. yazılı: "))
# sozlu = float(input("sözlü: "))
# ortalama = ((yazılı1 + yazılı2 + sozlu) / 3)

# if 0 <= ortalama <= 24:
#     print("not bilgisi: 0")
# elif 25 <= ortalama <= 44:
#     print("not bilgisi: 1")
# elif 45 <= ortalama <= 54:
#     print("not bilgisi: 2")
# elif 55 <= ortalama <= 84:
#     print("not bilgisi: 3")
# elif 85 <= ortalama <= 100:
#     print("not bilgisi: 5")

# from datetime import datetime
# suan = datetime.now()
# print(suan.date())

# yıl = int(input("çıkış yılı: "))
# suan = 2020
# if (suan - yıl) == 1:
#     print("1.bakım yılı")
# if (suan - yıl) == 2:
#     print("2.bakım yılı")
# else:
#     print("bakım süresi doldu")

import datetime
suan = datetime.datetime.now()
tarih = input("cıkıs tarihi (****/**/**): ")
tarih = tarih.split('/')
cıkıs = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
fark = suan - cıkıs
days = fark.days

if days<=365:
    print("1.servis")
elif 365 < days <= 365*2:
    print("2.servis")