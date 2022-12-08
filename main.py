import datetime as DT


#def str_to_date(self_date, other_date):
#    dt1 = self_date.split(".")
#    dt2 = other_date.split(".")
#    self_bdate = DT.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
#    other_bdate = DT.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
#    return self_bdate, other_bdate

#vin;gnum;mark;model;age;ls;km;count;price
class Car:
    def __init__(self, vin,gnum,mark,model,age,ls,km,count,price):
        self.vin = vin
        self.gnum = gnum
        self.mark = mark
        self.model = model
        self.age = age
        self.ls = ls
        self.km = km
        self.count = count
        self.price = price



    # Изменяем оклад
    def increase_salary(self, summa):
        self.salary += summa

    # Перехват функции print, когда она преобразует свое значение в строку
    def __str__(self):
        return f"Car {self.vin} {self.gnum}, {self.mark}," \
               f" CСтоимость: {self.price}, пробег: {self.price}"

    # Здесь и ниже операции сравнения >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate

    def __eq__(self, other):  # ==
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False
    def get_tax(self):
        if int(self.ls)<100:
            print('2000р')
        elif 150<int(self.ls)>100:
            print('3000р')
        elif 250 < int(self.ls) > 150:
            print('10000р')
    def get_age(self):
            print(self.age)
    def set_km(self,km):
            self.km=km
    def

class Owner:
    def __init__(self, fio,nud,datar,obl,cars):

        self.fio = fio
        self.nud = nud
        self.datar = datar


    # Добавляем сотрудника в отдел
    def append(self, emp):
        self.employees.append(emp)

    # Перехват функции print, когда она преобразует свое значение в строку
    # Возврат информации об отделе
    def __str__(self):
        return f"Отдел: {self.title}, Начальник: {self.chief.fio}, Количество сотрудников: {len(self.employees)} "

    # Вывод сотрудников отдела
    def print_employees(self):
        for emp in self.employees:
            print(emp)

    # Вывод сотрудников отдела в отпуске/не в отпуске
    def print_employees_on_leave(self, status=True):
        for emp in self.employees:
            if emp.on_leave == status:
                print(emp.number, emp.fio)


emp_1 = Car(1, 'Василий Иванович Гришкавец', '12.12.1970', 35000)
emp_2 = Car(2, 'Елизавета Петровна Кочедыкова', '17.10.1980', 33000)
# Сравним по датам рождения
print(emp_1 < emp_2)
print(emp_1 > emp_2)
print(emp_1 == emp_2)
print(emp_1 <= emp_2)
print(emp_1 >= emp_2)

depart_1 = Department('архив', emp_1)
depart_1.append(emp_1)
depart_1.append(emp_2)
print(depart_1)
depart_1.print_employees()
emp_1.increase_salary(1333)
emp_1.on_leave = True
emp_2.on_leave = True
print(emp_1)
depart_1.print_employees_on_leave()
