enesHesap = {
    "ad": "Enescan",
    "hesap no":"123",
    "bakiye": 3000,
    "ek hesap": 2000
}

def paracek(hesap, miktar):
    print(f"Merhaba {hesap['ad']} ")

    if hesap['bakiye'] >= miktar:
        hesap['bakiye'] -= miktar
        print(f"Paranızı alabilirsiniz.Kalan bakiye {hesap['bakiye']} tl dir.")

    else:
        toplam = hesap['bakiye'] + hesap['ek hesap']
        if toplam >= miktar:
            ekHesap = input("ek hesap kullanılsın mı? (e/h)")

            if ekHesap == "e":
                kulnlckmktr = miktar - hesap['bakiye']
                hesap['ek hesap'] -= kulnlckmktr
                print(f"paranızı alın. Kalan ek hesap limiti {hesap['ek hesap']} tl dir.")

            else :
                print(f"{hesap['hesap no']} nolu hesabınızda {hesap['bakiye']} tl bakiye vardır.")

        else:
            print("yetersiz bakiye")

paracek(enesHesap, 3000)
print('*********************')
paracek(enesHesap, 2000)
