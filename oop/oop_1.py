"""
ООП - Объектно-Ориентированное Программирование;
Класс - общее описание предметной области на языке программирования;
Объект - экземпляр (конкретный представитель класса);
Метод - функция, связанная с объектом класса / классом;
Аттрибут - характеристика (свойство) объекта или класса;
Конструктор - метод, который управляет созданием объекта;

Инкапсуляция - механизм, позволяющий скрывать внутренние детали реализации объекта
и предоставлять доступ к ним только через определённые методы, чтобы защитить
данные и контролировать доступ к ним;

"""

class Car:
    year = 2025
    _COLORS = ("red", "green", "blue")
    def __init__(self, brand, model, year, power, currency="RUB"):
        self.brand = brand
        self.model = model
        self.year = year
        self.power = power
        self.country = "Armenia"
        self.currency = currency
        self.is_power = False

        # Защищённый аттрибут
        self._color = "Black"

        # Приватный аттрибут
        self.__speed = None

    def go(self):
        if self.is_power:
            print(f"{self.brand} {self.model} TO GO")
        else:
            print("Car is not powered on!")

    def turn(self, direction):
        if self.is_power:
            print(f"{self.brand} {self.model} TURN {direction.upper()}")
        else:
            print("Car is not powered on!")

    def stop(self):
        if self.is_power:
            print(f"{self.brand} {self.model} STOP!")
        else:
            print("Car ")

    def power_on(self):
        if self.is_power:
            print("Car is already powered on!")
        else:
            print(f"{self.brand} {self.model} POWER ON!")
            self.is_power = True

    def power_off(self):
        if not self.is_power:
            print("Car is already powered off!")
        else:
            print(f"{self.brand} {self.model} POWER OFF!")
            self.is_power = False

    def display_color(self):
        print(self._color)

    def set_color(self, new_color):
        if new_color in Car._COLORS:
            self._color = new_color
        else:
            raise ValueError('Неправильный цвет')

    # Getter для получение значения скорости

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        if value > 300:
            raise ValueError("Max Speed = 300")
        self.__speed = value


class Truck(Car):
    # указывается характеристики родительские класса и новые классы дочерниго класса
    def __init__(self, brand, model, year, power, capasity, axles, currency="RUB"):
        # вызываем конструктор родительского класса с его параметрами через функцию super()
        super().__init__(brand, model, year, power, currency="RUB")
        self.capasity = capasity
        self.axles = axles
        self.__speed = 200

    def tilt_trailer(self):
        print(f"{self.brand} {self.model}")

car_audi = Car(brand="Audi", model="A6", year=2022, power=249)
car_bmw = Car(brand="BMW", model="X5", year=2022, power=349)
print(car_bmw.speed)
truck = Truck(brand="Volvo", model="XXX", year=2019, power=700, capasity=4000, axles=4)
truck.power_on()
truck.tilt_trailer()
truck.power_off()
truck.display_color()
truck.display_speed()
print(dir(truck))
# car_bmw.speed = 300
# car_audi.power_off()
# car_audi.go()
# car_audi.turn(direction="right")
# car_audi.power_on()
# car_audi.go()
# car_audi.turn(direction="right")
# car_audi.power_off()
