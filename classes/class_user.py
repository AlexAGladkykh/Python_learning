class User:
    def __init__(self):
        self.f_name = None
        self.m_name = None
        self.l_name = None
        self.age = None

    def input_fio(self):
        self.f_name = input("Input First Name: ")
        self.m_name = input("Input Middle Name: ")
        self.l_name = input("Input Last Name: ")

    def input_age(self):
        self.age = input("Input Age: ")

    def serialize(self):
        return "First name: {}\n" \
                "Middle name: {}\n"\
                "Last name: {}\n" \
                "Age : {}\n"\
                .format(self.f_name,self.m_name,self.l_name, self.age)
    
    def save(self):
        import json
        chel={}
        chel['First name']=self.f_name
        chel['Midle name']=self.m_name
        chel['Lasr name']=self.l_name
        chel['Age']=self.age
        fileName=input('Как хотите назвать файл (Формат: Имя.Расширение)? ')
        with open(fileName, "w") as f:
            json.dump(chel, f)
    
    def load(self):
        import json
        fileName=input('Введите имя файла: ')
        chel = {}
        with open(fileName, "rb") as f:
            chel = json.load(f)
        return chel


chelovek = User()
chelovek.input_fio()
chelovek.input_age()
print(chelovek.serialize())
chelovek.save()
chel={}
chel=chelovek.load()
print(chel)
print(chelovek)
