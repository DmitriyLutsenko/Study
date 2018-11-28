def Info():
    print("Разработчик: Луценко Дмитрий")
    print("Группа: 3-10-16-ИВТб")
    print("Лабораторная работа №4")
    print("Вариант работы: 11")
    print("Дисциплина: Программирование роботехнических комплексов")
    print("Тема: Рекурсия")
    print("Задание:")
    print("Вычислить функцию вычисления биноминальных коэффициентов С(m, n)")
    print("С(0, n) = C(n, n) = 1; C(m, n) = C(m, n - 1) + C(m - 1, n - 1); При 0 < m < n")

def C(m, n):
    if(m == n or m == 0 or n == 0 ):
        return 1
    else:
        result = C(m, n - 1) + C(m -1, n - 1)
        return result


def Input():
    m = int(input('Введите m >> '))
    n = int(input('Введите n >> '))
    print ("Вычисляем функцию биноминальных коэффициентов С(",m, ",", n,")")
    return m, n

Info()

m, n = Input()
result = C(m, n)
print ( "C(", m, ",", n,") = ", result)

