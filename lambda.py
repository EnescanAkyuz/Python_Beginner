# def square(num): return num ** 2 

# numbers = [1,3,5]
# for no in (map(square,numbers)):
#     print(no)



# numbers = [1,3,5]
# for iterm in map(lambda num: num ** 2, numbers):
#     print(iterm)



numbers = [1,2,5,7,10]
# def checkEven(a): return a%2==0
# result = list(filter(checkEven,numbers))
# print(result)

for item in filter(lambda num: num%2==0,numbers):
    print(item)