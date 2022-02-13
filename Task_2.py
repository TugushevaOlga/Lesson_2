new_list = list(input('Введите несколько чисел: '))
print(new_list)
for i in range(1, len(new_list), 2):
    new_list[i - 1], new_list[i] = new_list[i], new_list[i - 1]  # присваивание через кортеж
print(new_list)
#вариант решения
# снова поменяем с помощью методов списка insert и pop
for i in range(1,len(new_list),2):
    new_list.insert(i-1,new_list.pop(i))
print(new_list)


