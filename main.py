"""
Задание #1: Создайте структуру с именем student, содержащую поля: фамилия и инициалы, номер группы, успеваемость
(массив из пяти элементов). Создать массив из десяти элементов такого типа, упорядочить записи по возрастанию среднего
балла. Добавить возможность вывода фамилий и номеров групп студентов, имеющих оценки, равные только 4 или 5.
"""
import re
from typing import List


class Student:
    def __init__(self, name: str, group_number: str, grades: List[int]):
        self.name = name
        self.group_number = group_number
        self.grades = grades

    regular_name = '[А-Я][а-я]{1,20}\s[А-Я]\.[А-Я]\.'
    reg_name = re.compile(regular_name)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value, reg_name=reg_name):
        if isinstance(value, str) and reg_name.findall(value):
            self._name = value
        else:
            raise ValueError('name должен быть типом данных str и записан в формате Фамилия И.О.')

    @property
    def group_number(self):
        return self._group_number

    @group_number.setter
    def group_number(self, group):
        if isinstance(group, str):
            self._group_number = group
        else:
            raise ValueError('group_number должен быть типом данных str')

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, values):
        if isinstance(values, list) and len(values) == 5:
            for value in values:
                if 0 < value < 6:
                    self._grades = values
                else:
                    raise ValueError('grades must be 1-5')
        else:
            raise ValueError('grades должен быть типом данных list с длиной 5')

    def __lt__(self, other):
        return sum(self.grades) < sum(other.grades)


def show_students():
    for j in range(len(students)):
        print(f"ФИО: {students[j].name}, "
              f"Группа: {students[j].group_number}, "
              f"Оценки: {[x for x in students[j].grades]}\n")


def sort_by_average_score():
    students.sort()
    show_students()


def show_good_students():
    bad_grades = [1, 2, 3]
    for j in students:
        for value in j.grades:
            if value in bad_grades:
                break
        else:
            print(f"{j.name}")


students = []

if __name__ == '__main__':
    for i in range(0, 4):
        students_name = input(f'Введите для {i+1}-го ученика ФИО: ')
        students_group = input(f"Введите для {i+1}-го ученика группу: ")
        students_grades = [int(input(f'Введите {x+1}-ую оценку от 1 до 5: ')) for x in range(0, 5)]
        students.append(Student(students_name, students_group, students_grades))

    show_students()

    while True:
        controls = input("1 - упорядочить записи по возрастанию среднего балла учеников\n"
                         "2 - показать учеников, у которых оценки 4, 5\n"
                         "0 - выйти из программы\n-->")
        if controls == '1':
            sort_by_average_score()
        elif controls == '2':
            show_good_students()
        elif controls == '0':
            exit()
        else:
            print("Нет такого действия!")


"""
Задание #2: Создайте структуру с именем train, содержащую поля: название пункта назначения, номер поезда, время
отправления. Ввести данные в массив из пяти элементов типа train, упорядочить элементы по номерам поездов. Добавить
возможность вывода информации о поезде, номер которого введен пользователем. Добавить возможность сортировки массив по
пункту назначения, причем поезда с одинаковыми пунктами назначения должны быть упорядочены по времени отправления.
"""


class Train:
    def __init__(self, destination, train_number, departure_time):
        self.destination = destination
        self.train_number = train_number
        self.departure_time = departure_time

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if isinstance(value, str):
            self._destination = value
        else:
            raise ValueError('destination должен быть типом данных str')

    @property
    def train_number(self):
        return self._train_number

    @train_number.setter
    def train_number(self, value):
        if isinstance(value, int):
            self._train_number = value
        else:
            raise ValueError('train_number должен быть типом данных int')

    @property
    def departure_time(self):
        return self._departure_time

    @departure_time.setter
    def departure_time(self, value):
        if isinstance(value, str):
            self._departure_time = value
        else:
            raise ValueError('departure_time должен быть типом данных str')

    def __lt__(self, other):
        return self.train_number < other.train_number


trains = []
destination_list = []


def sort_by_train_number():
    trains.sort()
    for j in range(len(trains)):
        print(f"Номер поезда: {trains[j].train_number}, "
              f"отправка: {trains[j].departure_time}, "
              f"пункт назначения: {trains[j].destination}\n")


def sort_by_destination():
    sort_list = sorted(trains, key=lambda x: (x.destination[0], x.departure_time[0]))
    for j in range(len(sort_list)):
        print(f"Номер поезда: {sort_list[j].train_number}, "
              f"отправка: {sort_list[j].departure_time}, "
              f"пункт назначения: {sort_list[j].destination}\n")


if __name__ == '__main__':
    # train1 = Train('Lviv', 253, '18.40')
    # train2 = Train('Kyiv', 19, '12.30')
    # train3 = Train('Odesa', 456, '09.40')
    # train4 = Train('Rivne', 753, '20.10')
    # train5 = Train('Kyiv', 45, '06.35')
    #
    # trains = [train1, train2, train3, train4, train5]

    for i in range(0, 5):
        trains_destination = input(f'Введите для {i}-го поезда пункт назначения: ')
        trains_number = int(input(f'Введите для {i}-го поезда его номер: '))
        trains_departure_time = input(f'Введите для {i}-го поезда время отправления: ')
        trains.append(Train(trains_destination, trains_number, trains_departure_time))

    for i in range(len(trains)):
        print(f"Номер поезда: {trains[i].train_number}, "
              f"отправка: {trains[i].departure_time}, "
              f"пункт назначения: {trains[i].destination}\n")

    while True:
        controls = input("1 - посмотреть информацию о поезде\n"
                         "2 - отсортировать поезда по номерам\n"
                         "3 - отсортировать поезда по пунктам назначения\n"
                         "0 - выйти из программы\n-->")
        if controls == '1':
            number_of_train = input("Введите номер поезда, чтоб узнать о нем информацию: ")
            for i in range(len(trains)):
                if trains[i].train_number == int(number_of_train):
                    print(f"Номер поезда: {trains[i].train_number}, "
                          f"отправка: {trains[i].departure_time}, "
                          f"пункт назначения: {trains[i].destination}\n")
        elif controls == '2':
            sort_by_train_number()
        elif controls == '3':
            sort_by_destination()
        elif controls == '0':
            exit()
        else:
            print("Нет такого действия!")

"""
Задание #3:
Создайте класс Грузовик
У которого есть параметры Марка, год производства, максимальная скорость и кол-во км сколько ему нужно проехать
Класс должен уметь:
 - получать марку, год производства грузовика
 - получать за какое время грузовик проедет заданное количество км
"""


class Truck:
    def __init__(self, model, year, speed, distance):
        self.model = model
        self.year = year
        self.speed = speed
        self.distance = distance

    def get_info(self):
        print(f'{self.model}, год {self.year}')

    def get_time(self):
        print(f'Грузовик {self.model} проедет заданное количество км за {self.distance/self.speed} ч')


model_truck_1 = input("Введите модель грузовика: ")
year_truck_1 = int(input("Введите год производства грузовика: "))
speed_truck_1 = int(input("Введите максимальную скорость: "))
distance_truck_1 = int(input("Введите дистанцию, которую он должен проехать в км: "))

truck_1 = Truck(model_truck_1, year_truck_1, speed_truck_1, distance_truck_1)
truck_1.get_info()
truck_1.get_time()
