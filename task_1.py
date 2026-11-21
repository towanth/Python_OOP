class Bachelor:
    """Класс, содержащий информацию о студенте бакалавре."""

    def __init__(self, lastname: str = '-', speciality: str = '-', year: int = 1) -> None:
        """Метод инициализации объекта класса.

        Args:
            lastname: Фамилия
            speciality: Специальность
            year: Курс (от 1 до 4)
        """
        self.__lastname = lastname
        self.__speciality = speciality
        self.__year = year

    def set_lastname(self, lastname: str) -> None:
        """Сеттер фамилии.
        Args:
            lastname: Фамилия
        """
        if lastname and lastname.isalpha():
            self.__lastname = lastname
        else:
            print('Фамилия введена неверно')

    def get_lastname(self) -> str:
        """Геттер фамилии.

        :returns:
            str: Фамилия
        """

        return self.__lastname

    def set_speciality(self, speciality: str) -> None:
        """Сеттер специальности.
        Args:
            speciality: Специальность
        """
        if speciality and not speciality.isdigit():
            self.__speciality = speciality
        else:
            print('Специальность введена неверно')

    def get_speciality(self) -> str:
        """Геттер специальности.

        :returns:
            str: Специальность
        """

        return self.__speciality

    def set_year(self, year: int) -> None:
        """Сеттер курса.
        Args:
            year: Курс
        """
        if year and isinstance(year, int) and 1 <= year <= 4:
            self.__year = year
        else:
            print('Курс введён неверно')

    def get_year(self) -> int:
        """Геттер курса.
        :returns:
            int: Курс
        """

        return self.__year

    def show_info(self) -> None:
        """Вывод информации о студенте бакалавре."""

        print(
            f'Фамилия: {self.get_lastname()}\n',
            f'Специальность: {self.get_speciality()}\n',
            f'Курс: {self.get_year()}'
        )

    def promotion(self) -> None:
        """Переход на следующий курс."""

        if self.__year < 4:
            self.__year += 1
            print(f'Переход студента {self.get_lastname()} на курс {self.get_year()}')
        else:
            print(f'Студент {self.get_lastname()} выпустился')

    def years_until_graduation(self) -> None:
        """Сколько лет осталось до выпуска."""

        years_left = 4 - self.__year
        if years_left == 0:
            print(f'Студент {self.get_lastname()} на выпускном курсе')
        else:
            print(f'Студенту {self.get_lastname()} осталось (ся) {years_left} лет (год) до окончания бакалавриата')

class Menu:
    """Класс Меню."""

    def __init__(self, student: Bachelor) -> None:
        """Метод инициализации объекта класса.

            Args:
                student: экземпляр класса Bachelor
        """
        self.__student = student

    def run(self) -> None:
        """Вызов меню."""

        is_end = False

        while not is_end:
            print('\nМеню\n')
            print('1 - Показать информацию о студенте')
            print('2 - Изменить фамилию')
            print('3 - Изменить специальность')
            print('4 - Изменить курс')
            print('5 - Перевести студента на следующий курс')
            print('6 - Посчитать, сколько лет осталось до выпуска')
            print('0 - Завершить работу\n')

            input_str = input('Введите номер команды: \n')

            match input_str:
                case '0':
                    print('Завершение работы\n')
                    is_end = True
                case '1':
                    print('Текущие данные:\n')
                    self.__student.show_info()
                case '2':
                    lastname = input('Введите фамилию: ')
                    self.__student.set_lastname(lastname)
                case '3':
                    speciality = input('Введите специальность: ')
                    self.__student.set_speciality(speciality)
                case '4':
                    year = input('Введите курс: ')
                    self.__student.set_year(int(year))
                case '5':
                    self.__student.promotion()
                case '6':
                    self.__student.years_until_graduation()
                case _:
                    print('Неверно введённая команда\n')

student_1 = Bachelor('Петров', 'Программная инженерия', 1)
student_2 = Bachelor('Сидоров', 'Прикладная информатика', 3)

print('Два экземпляра класса для взаимодействия:\n')
print(f'student_1: {student_1.get_lastname()}, {student_1.get_speciality()}, {student_1.get_year()}\n')
print(f'student_2: {student_2.get_lastname()}, {student_2.get_speciality()}, {student_2.get_year()}\n')

print('Взаимодействие с student_1:')
Menu(student_1).run()

print('Взаимодействие с student_2:')
Menu(student_2).run()



