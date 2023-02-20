# 1. Создать класс под названием data, в класс
# добавить атрибуты full_name, email, file_name,
# color. Добавить геттеры и сеттеры для всех
# атрибутов
# 2. Затем считать из файла MOCK_DATA.txt, в
# котором 1000 строк с данными (Имя и Фамилия,
# почта, название файла с расширением и код
# цвета)
# 3. Из каждой считанной строки создать объект
# класса data и добавить его в список.
# 4. Затем через цикл пройтись по каждому
# объекту и записать в 4 разных файла все типы
# информации. (1й файл: Имена с фамилиями, 2й
# файл: почта, 3й файл: названия файлов с
# расширением, 4й файл: коды цветов)

import re

class Data:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name (self):
        return self.__file_name

    @full_name.setter
    def full_name(self, value):
        self.__file_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value 


with open("MOCK_DATA.txt", "r", encoding = "utf-8") as file:
    data = file.read()

    email_list = re.findall (r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+", data)
    print(len(email_list))
    print(email_list)

    file_list = re.findall(r"[A-Z]\w+\.\w+", data)
    print(len(file_list))
    print(file_list)


    color_list = re.findall(r"#\w+", data)
    print(len(color_list))
    print(color_list)

    # fio_list = re.findall(r"", data)
    # print(len(fio_list))
    # print(fio_list)

rezui = Data(email= email_list)
rezui_1 = Data(file_name= file_list)
rezui_2 = Data(color= color_list)

pole = [rezui, rezui_1, rezui_2]

for i in pole:
    print()