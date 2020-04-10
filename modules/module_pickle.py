import pickle

def toPickle(data):
    fileName=input('Как хотите назвать файл (Формат: Имя.Расширение)? ')
    with open(fileName, "wb") as f:
        pickle.dump(data, f)

def fromPickle(fileName=input('Введите имя файла: ')):
    data = {}
    with open(fileName, "rb") as f:
        data = pickle.load(f)
    return data

