#Задачка Корзина с грушами
class PearsBasket: #принимает количество груш в корзине
    def __init__(self, appl):
        self.appl = appl

    def __floordiv__(self, n): # Принимает количество детей между которыми Делит груши из корзины
        korzin = []
        m = self.appl // n
        for i in range(n):
            korzin.append(PearsBasket(m))
        if self.appl % n > 0:  # остатки груш в корзине
            korzin.append(PearsBasket(self.appl % n))
        return korzin    #выводит корзины детей и остатки в основной корзине

    def __mod__(self, n): #покажжем целочисленный остаток при делении
        return self.appl % n

    def __add__(self, n): # Складывает две корзинки
        return self.appl + n.appl

    def __sub__(self, n): # Съедаем груши пока не кончится
        return max(self.appl - n, 0)

    def __str__(self):
        return self.appl

    def __repr__(self):
        return "PearsBasket({})".format(self.appl)

# Проверочка
pb = PearsBasket(17)
array = pb // 4
print(array)
pb_2 = PearsBasket(13)
pb_3 = pb + pb_2
print(pb_3)
print(pb_3 % 7)
print(pb - 2)
print([pb])