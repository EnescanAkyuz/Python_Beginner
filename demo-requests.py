import requests
import json
url = "https://api.exchangeratesapi.io/latest?base="

bozulacak = input("bozdurmak istediğiniz tür: ")
verilecek = input("almak istediğiniz tür: ")
miktar = int(input("miktar: "))

result = requests.get(url+bozulacak)
result = json.loads(result.text)

print("Şuan 1 {0} = {1} {2}".format(bozulacak,result["rates"][verilecek],verilecek))
print("Size verilecek tutar ise {0} {1} = {2} {3}".format(miktar,bozulacak,miktar*result["rates"][verilecek],verilecek))