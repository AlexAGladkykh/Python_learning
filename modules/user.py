def newUserData():
    newUserData={}
    newUserData['Name']=input('Введите имя пользователя: ')
    newUserData['MidleName']=input('Введите отчество пользователя: ')
    newUserData['LastName']=input('Введите фамилию пользователя: ')
    newUserData['Age']=input('Ведите возраст пользователя: ')
    return newUserData



def serializeNewUserData(newUserData):
    dataAfterSer=   "Имя пользователя: {}, "\
                    "Отчество пользователя: {}, "\
                    "Фамилия пользователя: {}, "\
                    "Возраст пользователя: {}".format(newUserData['Name'],
                                                          newUserData['MidleName'],
                                                          newUserData['LastName'],
                                                          newUserData['Age'])
    return dataAfterSer

