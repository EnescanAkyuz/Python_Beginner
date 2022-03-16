sayilar = [1,3,5,7,9,12,19,21]

# i = 0
# while (i < len(sayilar)):
#     print(sayilar[i])
#     i += 1


# bas = int(input("başlangıç sayısı: "))
# son = int(input("bitiş sayısı: "))

# x = bas
# while (x < son):
#     x += 1
#     if x % 2 == 1:
#         print(x)

# x = 100
# while x > 0:
#     print(x)
#     x -= 1
    
# numbers = []
# i = 0
# while i<5:
#     sayi = int(input("sayı: "))
#     i+=1
#     numbers.append(sayi)
#     numbers.sort()

# print(numbers)

urunler = []
i = 0
adet = int(input("ürün sayısı: "))
while i<adet:
    name = input("ürün ismi: ")
    price = input("ürün fiyatı: ")
    urunler.append({
        "name": name,
        "price": price
    })
    i+=1
for urun in urunler:
    print(f"ürün adı:{urun['name']} ürün fiyatı: {urun['price']}")