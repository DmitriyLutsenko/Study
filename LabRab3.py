def Info():
    print("Разработчик: Луценко Дмитрий")
    print("Группа: 3-10-16-ИВТб")
    print("Лабораторная работа №3")
    print("Вариант работы: A11")
    print("Дисциплина: Программирование роботехнических комплексов")
    print("Тема: Работа со строками")
    print("Задание:")
    print("Все повысить регистр всех русских гласных")


def my_task(str):
    vowels = ["а", "о", "у", "ы", "и", "е", "э", "ю", "я", "ё"]
    res_str = ""
    for str_i in str:  # перебираем все буквы входного слова
        if str_i in vowels:  # проверяем, есть ли буква с писке главных и не повторяется ли она в результате
            res_str+=(str_i.upper())  # добавляем в результат
        else:
            res_str += str_i
    return res_str


Info()
str = str(input())
print(my_task(str))