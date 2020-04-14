import json

class Man:
    def __init__(self):
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.age = None

    def input_info(self):
        self.f_name = input("Input First Name: ")
        self.m_name = input("Input Middle Name: ")
        self.l_name = input("Input Last Name: ")
        self.age = input("Input Age: ")

    def man_info(self):
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
        with open("users.txt", "w") as f:
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
        with open("users.txt", "w") as f:
            data={}
            data['login']=self.login
            data['password']=self.password
            data['email']=self.email
            json.dump(data, f)
    
    def user_info(self):
        pass

user = User()
user.reg()
user.log()
user.input_info()
print(user.man_info())
user.save()





