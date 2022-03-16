class Circle:

    pi = 3.14

    def __init__(self, yaricap):
        self.yaricap = yaricap

    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap ** 2)

p1 = Circle(1)
p2 = Circle(5)

print(f"p1: çevre = {p1.cevre_hesapla()} ve alan {p1.alan_hesapla()}")
print(f"p2: çevre = {p2.cevre_hesapla()} ve alan {p2.alan_hesapla()}")