
def Info():
    print("Разработчик: Луценко Дмитрий")
    print("Группа: 3-10-16-ИВТб")
    print("Лабораторная работа №2")
    print("Вариант работы: С1")
    print("Дисциплина: Программирование роботехнических комплексов")
    print("Тема: Обработка списков")
    print("Задание:")
    print("Удалить четные элементы, стоящие после максимального")

def InputList():
    print('Вводите значения списка, нажимайте enter')
    print(' для окончания ввода просто нажмите enter')
    a = int(input('>>> '))
    Arr = []
    while True:
        try:
            Arr.append(a)
            a = int(input('>>> '))
        except:
            break
    return Arr

def deldev2(Arr):
    #Находим индекс максимального элемента списка
    i = Arr.index(max(Arr))
    #Здесь происходит конкатенация списка, что стоит перед максимальным,
    # включая максимальный со списком после максимального, где элементы нечетные
    new_list = Arr[:i + 1] + [j for j in Arr[i + 1:] if j % 2]
    return new_list


Info()
mylist=InputList()
print ("Исходный список: ", mylist)
mylist_1=deldev2(mylist)
print("Измененный список: ", mylist_1)

