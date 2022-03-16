ogrenciler = {}
number = input("öğrenci no : ")
name = input("öğrenci ad : ")
surname = input("öğrenci soyadı : ")
phone = input("öğrenci telefonu : ")

ogrenciler[number] = {
    'ad' : name,
    'soyad' : surname,
    'telefon' : phone
}

print(ogrenciler)




ogrNo = input("öğrenci no : ")
ogrenci = ogrenciler[ogrNo]

print(ogrenci)