# def yetki_sorgula(page):
#     def inner(role):
#         if role == "admin" :
#             print("{0} rolü {1} sayfasına ulaşabilir." .format(page, role))
#         else:
#             print("{0} rolü {1} sayfasına ulaşamaz." .format(page, role))
#     return inner

# user1 = yetki_sorgula('arayüz')
# print(user1("admin"))


def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi == "toplam":
        return toplam
    else:
        return carpma

toplama = islem("toplam")
print(toplama(1,3,5,7,9))