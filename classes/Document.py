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
         return "Registration number: {}\n"\
                "Year of manufacture: {}\n"\
                "Ovner surname: {}\n"\
                "Ovner name: {}\n"\
                "Ovner adress: {}\n"\
                "Make: {}\n" \
                "Type: {}\n"\
                "Commercial description: {}\n" \
                "VIN: {}\n" \
                "Maximum mass: {}\n"\
                "Vehicle category: {}\n"\
                "Capacity: {}\n"\
                "Color : {}\n"\
                "Number of seats: {}\n" \
                .format(self.d_RegNumber, self.d_YearOfM, self.l_name, self.f_name, self.d_Adress, 
                        self.a_make, self.a_type, self.a_com_descr, self.a_vin, self.a_max_mass, 
                        self.d_categ, self.a_capacity, self.a_color, self.a_num_of_seets)
    
    def save_f(self):
        info = self.show_info()
        with open("autos.txt", "w") as f:
            f.write(info)
            f.close()
    
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
        data['d.reg.num'] = self.d_RegNumber
        data['d.year.of.m'] = self.d_YearOfM
        data['l.name'] = self.l_name
        data['f.name'] = self.f_name
        data['d.categ'] = self.d_categ
        with open("autos.txt", "w") as f:
            json.dump(data, f)
            
    
    def load(self):
        data = {}
        with open("autos.txt", "r") as f:
            data = json.load(f)
            self.a_make = data['a.make'] 
            self.a_type = data['a.type'] 
            self.a_com_descr = data['a.com.deskr']
            self.a_color = data['a.color']
            self.a_vin = data['a.vin']
            self.a_capacity = data['a.cap']
            self.a_num_of_seets = data['a.n.of.s']
            self.a_max_mass = data['a.max.m']
            self.d_RegNumber = data['d.reg.num']
            self.d_YearOfM = data['d.year.of.m']
            self.l_name = data['l.name']
            self.f_name = data['f.name']
            self.d_categ = data['d.categ']

doc = RegCert()
doc.input_info()
print(doc.show_info())
doc.save()
print(doc.load())
