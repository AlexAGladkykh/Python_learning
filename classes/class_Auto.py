import json

class Auto:

    def __init__(self):
        self.a_make = None
        self.a_type = None
        self.a_com_descr = None
        self.a_color = None
        self.a_vin = None
        self.a_capacity= None
        self.a_num_of_seets = None
        self.a_max_mass= None


    def input_info(self):
        self.a_make = input("Ведите марку автомобиля: ")
        self.a_type = input("Введите модель автомобиля: ")
        self.a_com_descr = input("Введите тип кузова: ")
        self.a_color = input("Введите цвет автомобиля: ")
        self.a_vin = input("Введите VIN: ")
        self.a_capacity= input("Введите объем двигателя: ")
        self.a_num_of_seets = input("Введите колтчество мест в автомобиле: ")
        self.a_max_mass= input("Введите максимальную разрешенную массу: ")
        

    def show_info(self):
        return  "Марка: {}\n" \
                "Модель: {}\n"\
                "Тип кузова: {}\n" \
                "Цвет : {}\n"\
                "VIN: {}\n" \
                "Объем двигателя: {}\n"\
                "Колтчество мест: {}\n" \
                "Максимадьная разрешенная масса : {}\n"\
                .format(self.a_make,self.a_type,self.a_com_descr, self.a_color,
                        self.a_vin,self.a_capacity,self.a_num_of_seets, self.a_max_mass)
    
    def save(self):
        data={}
        data['a.make'] = self.a_make
        data['a.type'] = self.a_type
        data['a.com.deskr'] = self.a_com_descr
        data['a.color'] = self.a_color
        data['a.vin'] = self.a_vin
        data['a.cap'] = self.a_capacity
        data['a.n.of.s'] = self.a_num_of_seets
        data['a.max.m'] = self.a_max_mass
        with open("autos.txt", "a") as f:
            data_str = json.dumps(data)
            # json.dump(data, f)
            print(data_str)
            print(type(data_str))
            f.write(data_str)
            # f.write('\n')
            f.close()
    
    def load(self):
        data = {}
        with open("autos.txt", "rb") as f:
            data = json.load(f)
            self.a_make = data['a.make']
            self.a_type = data['a.type'] 
            self.a_com_descr = data['a.com.deskr'] 
            self.a_color = data['a.color']
            self.a_vin = data['a.vin']
            self.a_capacity = data['a.cap']
            self.a_num_of_seets = data['a.n.of.s']
            self.a_max_mass = data['a.max.m'] 
        
    
    def save_f(self):
        info = self.show_info()
        with open("autos.txt", "a") as f:
            f.write(info)
            f.close()


# fabia = Auto()
# fabia.input_info()
# print(fabia.show_info())
# fabia.save()
# print(fabia.load())
