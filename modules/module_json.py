import json

def toJson(data):
    fileName=input('Как хотите назвать файл (Формат: Имя.Расширение)? ')
    with open(fileName, "w") as f:
        json.dump(data, f)


def fromJson():
    fileName=input('Введите имя файла: ')
    data = {}
    with open(fileName, "rb") as f:
        data = json.load(f)
    return data
