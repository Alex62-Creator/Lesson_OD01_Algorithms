# 1 алгоритм
# Создаем пустую строку в которую поместим перевернутую исходную
# Вычисляем длину исходной строки
# Создаем цикл в котором будем перебирать символы исходной строки начиная с конца
# Текущий символ будем добавлять в конец результирующей строки
# Сравниваем исходную строку с результирующей
# При совпадении возвращаем True, иначе False

def is_palindrome1(s):
    result = ""
    size = len(s)

    while(size):
        result += s[size - 1]
        size -= 1

    return (s.lower() == result.lower())

print(is_palindrome1("Papap"))
print(is_palindrome1("papan"))


# 2 алгоритм
# Создаем цикл for с количеством итераций равным длине строки деленной на 2 с округлением до целого в большую сторону
# На каждой итерации сравниваем символ стоящий на i-й позиции с начала строки с символом стоящим на i-й позиции с конца строки
# Если находим не совпадение, возвращаем False
# После окончания цикла возвращаем True

import math

def is_palindrome2(s):
    for i in range(math.ceil(len(s)/2)):
        if s[i].lower() != s[len(s) - 1 - i].lower():
            return False
    return True

print(is_palindrome2("Как то или от как"))
print(is_palindrome2("как то или от как"))
print(is_palindrome2("как то если от как"))