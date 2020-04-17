import json
from class_Auto import Auto
from man import MaxUser

class RegCert(MaxUser, Auto):
    
    def __init__(self):
        self.RegNumber = None
        self.YearOfM = None
        self.Adress = None
        self.categ = None
        

    def input_info(self):
        MaxUser.input_info(self)
        self.d_Adress = input("Введите адрес владельца авто: ")
        Auto.input_info(self)
        self.d_RegNumber = input('Введите регистрационный номер авто: ')
        self.d_YearOfM = input("Введите год выпуска авто: ")
        self.d_categ = input("Введите категорию авто: ")
        
        

    def show_info(self):
         return "Регистоационный номер: {}\n"\
                "Год выпуска авто: {}\n"\
                "Фамилия владельца: {}\n"\
                "Имя владельца: {}\n"\
                "Адрес владельца: {}\n"\
                "Марка: {}\n" \
                "Модель: {}\n"\
                "Тип кузова: {}\n" \
                "VIN: {}\n" \
                "Максимадьная разрешенная масса : {}\n"\
                "Категория автомобиля: {}\n"\
                "Объем двигателя: {}\n"\
                "Цвет : {}\n"\
                "Количество мест: {}\n" \
                .format(self.d_RegNumber, self.d_YearOfM, self.l_name, self.f_name, self.d_Adress, 
                        self.a_make, self.a_type, self.a_com_descr, self.a_vin, self.a_max_mass, 
                        self.d_categ, self.a_capacity, self.a_color, self.a_num_of_seets)
    
    

doc = RegCert()
doc.input_info()
print(doc.show_info())