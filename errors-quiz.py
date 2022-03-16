liste = ["1","2","5","2a","10a","abc","20","50"]

# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except:
#         continue

# while True:
#     sayi = (input('sayı: '))
#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print('girdiğiniz sayı: ', result)
#     except ValueError:
#         print('girdi hatası')
        

# def checkPassword(parola):
#     trKarakter = 'ğüşıçöİ'

#     for i in parola:
#         if i in trKarakter:
#             raise TypeError('Türkçe karaktrer hatası.')
#         else:
#             pass
    
#     print('geçerli parola')        

# parola = input('parola: ')

# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)