# Объектно-ориентированное программирование (ООП) и SOLID в Python
Задание на изучение ООП в языке Python

# Задача
- В качестве практической работы необходимо нарисовать блок-схемы работы алгоритма решения задач и загрузить в свой репозиторий в течение дня.
- В качестве домашней работы необходимо реализовать программы по ранее созданным алгоритмам решения задач на языке Python и загрузить в свой репозиторий до крайнего срока.

Даты сдачи оговариваются в канале группы.

## Содержание

1.  [Что такое ООП](#1-что-такое-ооп)
2.  [Классы и объекты](#2-классы-и-объекты)
3.  [Атрибуты и методы](#3-атрибуты-и-методы)
4.  [Четыре принципа ООП](#4-четыре-принципа-ооп)
5.  [Дополнительные возможности
    Python](#5-дополнительные-возможности-python)
6.  [Что такое SOLID](#6-что-такое-solid)
7.  [Пять принципов SOLID](#7-пять-принципов-solid)
8.  [Как ООП и SOLID применяются
    вместе](#8-как-ооп-и-solid-применяются-вместе)

------------------------

# Теоретическая справка
## 1. Что такое ООП

**Объектно-ориентированное программирование (ООП)** - это подход к
созданию программ, при котором программа состоит из объектов. Объекты
объединяют данные и действия, которые можно выполнять над этими данными.

Представим, что мы пишем программу для библиотеки. В ней могут быть:

-   книга;
-   читатель;
-   библиотекарь;
-   запись о выдаче книги.

У книги есть данные: название, автор, год издания. С книгой можно
выполнять действия: показать информацию, проверить доступность, выдать
читателю.

В ООП данные и связанные с ними действия удобно объединить в одном
объекте.

### Зачем нужно ООП

ООП помогает:

-   упорядочить большой объём кода;
-   объединять связанные данные и операции;
-   повторно использовать готовые решения;
-   постепенно расширять программу;
-   проще проверять и поддерживать код.

ООП полезно не для каждой задачи. Небольшую программу иногда проще
написать с помощью обычных функций. Но когда в программе много сущностей
и взаимодействий, классы могут сделать структуру понятнее.

## 2. Классы и объекты

### 2.1. Класс

**Класс** - это описание того, какими данными и действиями будут
обладать объекты.

Например, класс `Student` описывает студента:

``` python
class Student:
    pass
```

Пока класс пустой. Добавим имя, группу и метод, который выводит
приветствие:

``` python
class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def introduce(self):
        print(f"Меня зовут {self.name}, я учусь в группе {self.group}.")
```

### 2.2. Объект

**Объект** - это конкретный экземпляр класса.

``` python
student1 = Student("Анна", "ПИ-101")
student2 = Student("Иван", "ПИ-102")

student1.introduce()
student2.introduce()
```

Результат:

``` text
Меня зовут Анна, я учусь в группе ПИ-101.
Меня зовут Иван, я учусь в группе ПИ-102.
```

Класс один, но объектов может быть много. У каждого объекта свои
значения атрибутов.

### 2.3. Что такое `self`

`self` - это ссылка на текущий объект. Через `self` метод обращается к
данным конкретного экземпляра.

``` python
class Student:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)
```

Когда мы вызываем `student1.show_name()`, Python автоматически передаёт
объект `student1` в параметр `self`.

Имя `self` - общепринятое соглашение Python. Обычно его не заменяют
другим именем.

### 2.4. Что делает `__init__`

`__init__` - специальный метод, который вызывается после создания
объекта и помогает задать его начальное состояние.

``` python
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


book = Book("Маленький принц", "Антуан де Сент-Экзюпери")
print(book.title)
```

Важно: `__init__` инициализирует объект, а не создаёт его на низком
уровне. За создание отвечает `__new__`, который новичкам обычно
достаточно просто узнавать по названию.

## 3. Атрибуты и методы

**Атрибуты** хранят данные объекта или класса. **Методы** описывают
действия, которые объект может выполнять.

### 3.1. Атрибуты экземпляра

У каждого объекта собственные значения:

``` python
class Student:
    def __init__(self, name):
        self.name = name


first = Student("Мария")
second = Student("Олег")

print(first.name)   # Мария
print(second.name)  # Олег
```

### 3.2. Атрибуты класса

Атрибут класса задаётся непосредственно в теле класса и является общим
значением по умолчанию для его экземпляров.

``` python
class Student:
    university = "Технический университет"

    def __init__(self, name):
        self.name = name


student = Student("Мария")

print(student.university)
print(Student.university)
```

Не стоит хранить в атрибутах класса изменяемые данные, которые должны
быть отдельными у каждого объекта.

Неправильно:

``` python
class Student:
    marks = []  # Список будет общим для всех объектов
```

Правильно:

``` python
class Student:
    def __init__(self):
        self.marks = []  # У каждого студента свой список
```

### 3.3. Методы

Метод - это функция, определённая внутри класса.

``` python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


rectangle = Rectangle(5, 3)
print(rectangle.area())  # 15
```

### 3.4. Три вида методов

**Обычный метод** получает объект через `self`:

``` python
class Student:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Привет! Я {self.name}."
```

**Метод класса** помечается `@classmethod` и получает класс через `cls`.
Он может использоваться, например, для создания объекта альтернативным
способом:

``` python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name, int(age))


student = Student.from_string("Ирина,19")
```

**Статический метод** помечается `@staticmethod`. Он не получает
автоматически ни объект, ни класс:

``` python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(2, 3))  # 5
```

На первом этапе достаточно запомнить: обычный метод работает с объектом,
`classmethod` - с классом, а `staticmethod` - это функция, логически
связанная с классом.

## 4. Четыре принципа ООП

Часто выделяют четыре основных принципа ООП:

1.  инкапсуляция;
2.  наследование;
3.  полиморфизм;
4.  абстракция.

### 4.1. Инкапсуляция

**Инкапсуляция** - объединение данных и методов работы с ними внутри
объекта, а также организация контролируемого доступа к внутреннему
состоянию объекта.

Например, банковский счёт не должен позволять списывать сумму,
превышающую баланс.

``` python
class BankAccount:
    def __init__(self, owner, balance):
        if balance < 0:
            raise ValueError("Начальный баланс не может быть отрицательным")

        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self._balance:
            raise ValueError("Недостаточно средств")
        self._balance -= amount


account = BankAccount("Алексей", 1000)
account.deposit(500)
account.withdraw(200)

print(account.balance)  # 1300
```

В Python есть соглашения об именовании:

-   `name` - публичный атрибут, его можно использовать извне;
-   `_name` - атрибут для внутреннего использования по соглашению;
-   `__name` - имя преобразуется механизмом `name mangling`, чтобы
    уменьшить риск конфликтов имён.

Одинарное и двойное подчёркивание не обеспечивают абсолютную защиту
данных. В Python разработчики в значительной степени полагаются на
соглашения.

Декоратор `@property` позволяет обращаться к методу как к атрибуту. Он
удобен, когда чтение или изменение значения нужно контролировать.

### 4.2. Наследование

**Наследование** позволяет создать новый класс на основе существующего.
Новый класс получает доступ к его атрибутам и методам и может добавлять
или изменять поведение.

``` python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} ест")


class Dog(Animal):
    def bark(self):
        print("Гав!")


dog = Dog("Бобик")
dog.eat()
dog.bark()
```

`Dog` наследуется от `Animal`, поэтому собака умеет выполнять метод
`eat()`.

#### Переопределение метода

Дочерний класс может предоставить собственную реализацию метода
родителя:

``` python
class Animal:
    def make_sound(self):
        print("Неизвестный звук")


class Cat(Animal):
    def make_sound(self):
        print("Мяу!")


cat = Cat()
cat.make_sound()
```

#### Функция `super()`

`super()` позволяет вызвать следующую реализацию метода в порядке поиска
методов (MRO). В простом случае это часто используется для вызова метода
родительского класса.

``` python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed


dog = Dog("Рекс", "Овчарка")
print(dog.name)
print(dog.breed)
```

### 4.3. Полиморфизм

**Полиморфизм** - возможность обращаться к объектам разных классов
через одинаковый способ взаимодействия, при этом каждый объект выполняет
действие по-своему.

``` python
class Dog:
    def make_sound(self):
        return "Гав!"


class Cat:
    def make_sound(self):
        return "Мяу!"


class Cow:
    def make_sound(self):
        return "Му!"


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    print(animal.make_sound())
```

Функции или циклу не нужно знать точный класс каждого объекта.
Достаточно, чтобы у объекта был нужный метод.

#### Duck Typing

В Python распространён подход Duck Typing: важнее то, какие действия
умеет выполнять объект, чем то, к какому классу он относится.

``` python
class PdfDocument:
    def save(self):
        print("Сохраняем PDF")


class TextDocument:
    def save(self):
        print("Сохраняем текстовый файл")


def save_document(document):
    document.save()


save_document(PdfDocument())
save_document(TextDocument())
```

Оба объекта подходят функции, потому что у каждого есть метод `save()`.

### 4.4. Абстракция

**Абстракция** - выделение главных возможностей объекта и сокрытие
ненужных пользователю деталей реализации.

Например, водителю достаточно знать, как управлять автомобилем. Ему не
нужно каждый раз разбираться во всех внутренних механизмах двигателя.

В Python абстрактные классы можно создавать с помощью модуля `abc`:

``` python
from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")


payment = CardPayment()
payment.pay(500)
```

Абстрактный класс задаёт общий контракт. Нельзя создать экземпляр
`Payment`, пока не реализованы его абстрактные методы.

### 4.5. Абстракция и инкапсуляция: различие

-   **Абстракция** показывает, какие возможности предоставляет объект,
    не раскрывая все детали.
-   **Инкапсуляция** объединяет данные и поведение и помогает
    контролировать доступ к внутреннему состоянию.

Например, кнопка банкомата предоставляет понятную операцию снятия денег
(абстракция), а проверка баланса и правил списания защищает состояние
счёта (инкапсуляция).

## 5. Дополнительные возможности Python

### 5.1. Композиция

**Композиция** - создание объекта, который создаёт другие объекты
как свои компоненты с сильной связью (Объекты создаются внутри нашего класса).

Пример: автомобиль содержит двигатель.

``` python
class Engine:
    def start(self):
        print("Двигатель запущен")


class Car:
    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print("Автомобиль готов к поездке")


car = Car()
car.start()
```

### 5.2. Агрегация

**Агрегация** - создание объекта, который использует другие объекты
как свои компоненты со слабой связью (Объекты создаются вне нашего класса).

Пример: Книга содержит автора.

``` python
class Author:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

author = Author("Антуан де Сент-Экзюпери")
book = Book("Маленький принц", author)
print(book.author.print_name())
```

Разница:

-   наследование - отношение «является»;
-   композиция - отношение «содержит».
-   агрегация - отношение «использует»

Автомобиль не является двигателем, но использует двигатель.

Композиция часто удобнее наследования, если объекту нужно использовать
готовую функциональность другого объекта.

### 5.3. Специальные методы

В Python есть специальные методы, имена которых начинаются и
заканчиваются двумя подчёркиваниями. Их называют dunder methods.

  Метод        Для чего нужен
  ---- ---------------
  `__init__`   Инициализация объекта
  `__str__`    Удобное текстовое представление
  `__repr__`   Представление объекта для разработчика
  `__len__`    Поведение функции `len()`
  `__eq__`     Поведение оператора `==`
  `__add__`    Поведение оператора `+`
  `__iter__`   Получение итератора
  `__next__`   Получение следующего элемента итератора

Пример:

``` python
class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Книга: {self.title}"


book = Book("Приключения Тома Сойера")
print(book)
```

Метод `__str__` позволяет определить, что будет выведено при
преобразовании объекта в строку.

### 5.4. Dataclasses

Если класс в основном хранит данные, можно воспользоваться `dataclass`.
Этот инструмент автоматически создаёт некоторые стандартные методы.

``` python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    age: int
    group: str


student = Student("Анна", 18, "ПИ-101")
print(student)
```

Аннотации типов помогают понять, какие значения ожидаются, но сами по
себе не обеспечивают строгую проверку типов во время выполнения.

## 6. Что такое SOLID

**SOLID** - пять принципов проектирования программ, которые помогают
делать код понятнее, гибче и удобнее для изменения.

Название SOLID образовано первыми буквами английских названий принципов:

  -------------------------
  **Буква - Название - Перевод**
  --------- --------- ---------
  **S - Single Responsibility Principle - Принцип единственной ответственности**
   
  **O - Open/Closed Principle - Принцип открытости/закрытости**

  **L - Liskov Substitution Principle - Принцип подстановки Барбары Лисков**

  **I - Interface Segregation Principle - Принцип разделения интерфейсов**

  **D - Dependency Inversion Principle - Принцип инверсии зависимостей**
                                         
  -------------------------

Необязательно применять все принципы в каждой маленькой программе. Их
смысл - помогать проектировать систему, а не заставлять создавать
лишние классы.

## 7. Пять принципов SOLID

### 7.1. S - Single Responsibility Principle (SRP)

**Принцип единственной ответственности:** у класса должна быть одна
основная ответственность и одна логическая причина для изменения.

Плохой пример:

``` python
class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        print("Сохраняем студента в базу")

    def send_email(self):
        print("Отправляем письмо")

    def create_report(self):
        print("Создаём отчёт")
```

Класс одновременно хранит данные, работает с базой, отправляет письма и
формирует отчёты.

Лучше разделить задачи:

``` python
class Student:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class StudentRepository:
    def save(self, student):
        print(f"Сохраняем студента {student.name}")


class EmailService:
    def send(self, student):
        print(f"Отправляем письмо на {student.email}")


class ReportService:
    def create(self, student):
        print(f"Создаём отчёт для {student.name}")
```

Теперь у каждого класса своя задача.

**Запомнить:** не нужно помещать всю программу в один огромный класс.

### 7.2. O - Open/Closed Principle (OCP)

**Принцип открытости/закрытости:** программные компоненты должны быть
открыты для расширения, но по возможности закрыты для изменения уже
работающего кода.

Плохой пример:

``` python
class NotificationService:
    def send(self, notification_type, message):
        if notification_type == "email":
            print(f"Email: {message}")
        elif notification_type == "sms":
            print(f"SMS: {message}")
```

При добавлении нового типа уведомления придётся менять метод `send()`.

Более гибкий вариант:

``` python
from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class EmailNotification(Notification):
    def send(self, message):
        print(f"Email: {message}")


class SmsNotification(Notification):
    def send(self, message):
        print(f"SMS: {message}")


class NotificationService:
    def __init__(self, notification):
        self.notification = notification

    def notify(self, message):
        self.notification.send(message)
```

Теперь можно добавить новый класс `PushNotification`, не меняя
`NotificationService`.

**Запомнить:** новую возможность желательно добавлять отдельным
компонентом, не переписывая проверенный код.

### 7.3. L - Liskov Substitution Principle (LSP)

**Принцип подстановки Барбары Лисков:** объект дочернего класса должен
корректно заменять объект родительского класса там, где ожидается
родительский тип.

Плохой пример:

``` python
class Bird:
    def fly(self):
        print("Птица летит")


class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Пингвин не летает")
```

Проблема: класс `Bird` обещает, что птица умеет летать, но пингвин не
может выполнить это действие.

Лучше разделить возможности:

``` python
class Bird:
    def eat(self):
        print("Птица ест")


class FlyingBird(Bird):
    def fly(self):
        print("Птица летит")


class Sparrow(FlyingBird):
    pass


class Penguin(Bird):
    pass
```

Теперь пингвин не наследует неподходящий метод `fly()`.

**Запомнить:** наследник не должен нарушать ожидания, которые задаёт
родительский класс.

### 7.4. I - Interface Segregation Principle (ISP)

**Принцип разделения интерфейсов:** не нужно заставлять класс
реализовывать методы, которые ему не нужны.

Плохой пример:

``` python
class Machine:
    def print_document(self):
        pass

    def scan_document(self):
        pass

    def fax_document(self):
        pass


class SimplePrinter(Machine):
    def print_document(self):
        print("Печать")

    def scan_document(self):
        raise NotImplementedError

    def fax_document(self):
        raise NotImplementedError
```

Обычный принтер умеет печатать, но не умеет сканировать и отправлять
факсы.

Лучше разделить интерфейсы:

``` python
class Printer:
    def print_document(self):
        raise NotImplementedError


class Scanner:
    def scan_document(self):
        raise NotImplementedError


class SimplePrinter(Printer):
    def print_document(self):
        print("Печать документа")


class MultiFunctionDevice(Printer, Scanner):
    def print_document(self):
        print("Печать документа")

    def scan_document(self):
        print("Сканирование документа")
```

Теперь каждый класс реализует только нужные ему операции.

**Запомнить:** лучше несколько небольших интерфейсов, чем один огромный.

### 7.5. D - Dependency Inversion Principle (DIP)

**Принцип инверсии зависимостей:** важная бизнес-логика не должна быть
жёстко привязана к конкретным техническим деталям. Обе части должны
зависеть от абстракции.

Плохой пример:

``` python
class MySQLDatabase:
    def save(self, data):
        print(f"Сохраняем в MySQL: {data}")


class StudentService:
    def __init__(self):
        self.database = MySQLDatabase()

    def save_student(self, student):
        self.database.save(student)
```

`StudentService` самостоятельно создаёт `MySQLDatabase`. Поэтому
заменить базу данных или подменить её при тестировании сложнее.

Более гибкий вариант:

``` python
from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass


class MySQLDatabase(Database):
    def save(self, data):
        print(f"Сохраняем в MySQL: {data}")


class StudentService:
    def __init__(self, database: Database):
        self.database = database

    def save_student(self, student):
        self.database.save(student)


database = MySQLDatabase()
service = StudentService(database)
service.save_student("Анна")
```

Теперь зависимость передаётся извне. Это называется **Dependency
Injection (внедрение зависимостей)**.

Важно различать:

-   DIP - принцип проектирования;
-   DI - способ передать объекту необходимые зависимости.

**Запомнить:** основной код должен зависеть от того, что компонент умеет
делать, а не от конкретной технологии, с помощью которой он это делает.

## 8. Как ООП и SOLID применяются вместе

Представим, что мы разрабатываем небольшую программу для
интернет-магазина. Она должна оформлять заказ и принимать оплату.

``` python
from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата картой: {amount}")
        return True


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Оплата наличными: {amount}")
        return True


class OrderRepository:
    def save(self, order):
        print(f"Заказ сохранён: {order}")


class OrderService:
    def __init__(self, repository, payment_method):
        self.repository = repository
        self.payment_method = payment_method

    def create_order(self, order, amount):
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")

        paid = self.payment_method.pay(amount)

        if not paid:
            raise RuntimeError("Оплата не прошла")

        self.repository.save(order)


repository = OrderRepository()
payment = CardPayment()

service = OrderService(repository, payment)
service.create_order({"id": 1, "product": "Книга"}, 500)
```

В этом небольшом примере используются разные идеи:

-   **Инкапсуляция:** логика оформления заказа находится внутри
    `OrderService`.
-   **Абстракция:** `PaymentMethod` задаёт общий интерфейс оплаты.
-   **Полиморфизм:** можно использовать `CardPayment` или `CashPayment`.
-   **Композиция:** сервис использует репозиторий и платёжный объект.
-   **SRP:** сохранение заказа и оплата вынесены в отдельные компоненты.
-   **OCP:** можно добавить новый способ оплаты.
-   **DIP:** сервис получает зависимости извне и работает с общим
    интерфейсом оплаты.

Это учебная версия. В реальном магазине дополнительно понадобятся
транзакции, обработка ошибок платёжной системы и защита от повторной
оплаты.
