"""
Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего.
Если таких слов несколько, выведите последнее.

Задачу необходимо решить с использованием словаря.
"""

dictionary = {}

text = '''She sells sea shells on the sea shore;
          The shells that she sells are sea shells I'm sure.
           So if she sells sea shells on the sea shore,
           I'm sure that the shells are sea shore shells.
        '''.split()     # разбираем строку на элементы "split()"
for i in range(len(text)):
    for j in text:                                 # проходим по тексту
        dictionary[j] = dictionary.get(j, 0) + 1   # считаем значение для ключа "get()"
maximum = max(dictionary.values())                 # вычисляем mах количество значений
lst = set()                                        # создаем пустое множество
for key in dictionary:                             # проходим по словарю
    if dictionary[key] == maximum:                 # проверяем, равел ли ключ mах значению
        lst.add(key)                               # max значение помещаем во множество
        s = sorted(lst)
print(s[-1])                                       # выводим последний элемент
