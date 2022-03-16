# def changename(n):
#     n = 'enes'

# name = 'musab'
# changename(name)
# print(name)

def ad(*params):
    a = 0

    for n in params:
        a = n + a

    return a

print(ad(10,20))            