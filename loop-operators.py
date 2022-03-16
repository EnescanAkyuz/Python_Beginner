# string = 'hello'
# list = []
# for result in string:
#     list.append(result)
# print(list)
#                                             #bu iki işlem aynı
# mylist = [result for result in string]
# print(mylist)

# years = [2002,1976,1979,2007,1956]
# age = [2020-year for year in years]
# print(age)

numbers = []
for x in range(2):
    for y in range(2):
        numbers.append((x,y))
print(numbers) 