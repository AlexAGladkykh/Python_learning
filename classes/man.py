import json

class Man:
    def __init__(self):
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.age = None

    def input_info(self):
        self.f_name = input("Введите имя: ")
        self.m_name = input("Введите отчество: ")
        self.l_name = input("Введите фамилию: ")
        self.age = input("Введите возраст: ")

    def show_info(self):
        return "First name: {}\n" \
                "Middle name: {}\n"\
                "Last name: {}\n" \
                "Age : {}\n"\
                .format(self.f_name,self.m_name,self.l_name, self.age)
    
    def save(self):
        data={}
        data['f.name']=self.f_name
        data['m.name']=self.m_name
        data['l.name']=self.l_name
        data['age']=self.age
        with open("users.txt", "a") as f:
            json.dump(data, f)
    
    def load(self):
        data = {}
        with open("users.txt", "rb") as f:
            data = json.load(f)
            self.f_name = data['f.name']
            self.m_name = data['m.name']
            self.l_name = data['l.name']
            self.age = data['age']

class User(Man):

    def __init__(self):
        self.login = None
        self.password = None
        self.conf_password=None
        self.email = None
        self.phone = None
        super().__init__(self)

    def log(self):
        login = input("Enter your login: ")
        password = input("Enter your password: ")
        with open("users.txt", "rb") as f:
            data = json.load(f)
            self.login=data['login']
            self.password=data['password']
        if self.login == login and self.password == password:
            print('Correct')
        else: print('Incorrect login or password')
        

    
    def reg(self):
        self.login = input("Input your login: ")
        self.password = input("Input your password: ")
        self.conf_password=input("Confirm your password: ")
        self.email = input("Input your email: ")
        super().input_info()
        with open("users.txt", "w") as f:
            data={}
            data['login']=self.login
            data['password']=self.password
            data['email']=self.email
            json.dump(data, f)

class MaxUser(User):
    
    def __init__(self):
        self.gender = None
        super().__init__(self)

    def reg(self):
        super().reg()
        self.gender=input("Enter your gender: ")

    
    def show_info(self):
        return  "User: {}\n"\
                "First name: {}\n" \
                "Middle name: {}\n"\
                "Last name: {}\n" \
                "Gender: {}\n"\
                "Age : {}\n"\
                .format(self.login, self.f_name,self.m_name,self.l_name, self.gender, self.age)    
    





