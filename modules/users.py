from user import * 
import json

users={}
def addUser():
    key=1
    isTrue=True
    while isTrue==True:
        if key not in users:
            users[key]=newUserData()
            test=input('Если хотите добавить следующего пользователя введите "Да" ')
            if test=='Да':
                key+=1
            else: isTrue=False
        elif key in users:
            key+=1
    return users
    
def listOfUsers(users):
    for key in users:
        print(serializeNewUserData(users[key]))

def delTheUser():
    char=input('Какого пользователя удалить? ')
    for number in users:
        if number==char:
            del users[number]
            return users
            break
        else:
             for description in users[number].keys():
                if users[number][description] == char:
                    del users[number]
                    return users
                    break
               
def updateInfo(number):
    isTrue=True
    while isTrue==True:
        char1=input('Что хотите обновить?(Имя/Отчество/Фамилия/Возраст. Введите что-то одно):  ')
        if char1=='Имя':
            users[number]['Name']=input('Введите новое имя: ')
        elif char1=='Отчество':
            users[number]['MidleName']=input('Введите новое отчество: ')
        elif char1=='Фамилия':
            users[number]['LastName']=input('Введите новую фамилию: ')
        elif char1=='Возраст':
            users[number]['Age']=input('Введите новый возраст: ')
        if input('Хотите закончить обновление информации - Да'):
            isTrue = False
    return users
            

def updateUserInfo():
    char=input('Введите номер или имя позьзователя, чью информацию желаете обновить: ')
    for number in users:
        if number==char:
            updateInfo(number)
            return users
            break
        else: 
            for description in users[number].keys():
                if users[number][description] == char:
                    updateInfo(number)
                    return users
                    break

def toJson(users):
    fileName=input('Как хотите назвать файл (Формат: Имя.Расширение)? ')
    with open(fileName, "w") as f:
        json.dump(users, f)


def fromJson():
    fileName=input('Введите имя файла: ')
    data = {}
    with open(fileName, "rb") as f:
        data = json.load(f)
    return data



