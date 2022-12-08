
from datetime import date


class Car:
    def __init__(self, vin, gnum, mark, model, age, ls, km, count, price):
        self.vin = vin
        self.gnum = gnum
        self.mark = mark
        self.model = model
        self.age = age
        self.ls = ls
        self.km = km
        self.count = count
        self.price = price

    # Изменяем пробег
    def increase_km(self, km):
        self.km += km

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"Car {self.vin} {self.gnum}, {self.mark}," \
               f" CСтоимость: {self.price}, пробег: {self.price}"

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_bdate, other_bdate = int(self.km), int(other.km)
        return self_bdate < other_bdate

    def __eq__(self, other):  # ==
        self_bdate, other_bdate = int(self.km), int(other.km)
        return self_bdate == other_bdate

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False

    # Пример расчета налога упрощенно
    def get_tax(self):
        if int(self.ls) < 100:
            print('2000р')
        elif 150 < int(self.ls) > 100:
            print('3000р')
        elif 250 < int(self.ls) > 150:
            print('10000р')

    def get_age(self):
        today = date.today()
        return (today.year - self.age) - ((today.month, today.day) < (self.month, self.day))
        # return today.year - born.year


class Owner:
    def __init__(self, fio, nud, datar, obl, cars=[]):
        self.fio = fio
        self.nud = nud
        self.datar = datar
        self.obl = obl
        self.cars = cars


    def __str__(self):
        return f"Владелец: {self.fio}, Номер удостоверения: {self.nud}, Авто: {len(self.cars)} "


    def add_car(self,car):
        self.cars.append(car)

    def get_cars(self):
        return f"В наличии: {self.cars}"


car_1 = Car(123123123, 'ТР103Т', 'Lada', 'Granta', '12.12.2021', 115, 15000, 1, 750000)
car_2 = Car(321321321, 'КК111С', 'Hyndai', 'i30', '12.12.2020', 135, 55000, 2, 1000000)

# Сравним по датам
print(car_1 < car_2)
print(car_1 > car_2)
print(car_1 == car_2)
print(car_1 <= car_2)
print(car_1 >= car_2)

vlad = Owner("Семен Семеныч", 63150013, "11.02.1990", 63)

print(vlad)
print('Накидываем авто')
vlad.add_car(str('КК111С'))
vlad.add_car(str('EE222E'))

print(vlad)

print(vlad.get_cars())

