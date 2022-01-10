import operator


def f(n):
    if n == 0:
        return 1
    return f(n-1) * n

dict = {'K': f(11), 'O': f(15), 'Z': f(26), 'L': f(12), 'O': f(15), 'V': f(22), 'A': f(1)}
print(dict)
#Первое задание

sorted_dict = sorted(dict.items())

print(sorted_dict)

file_to_save = open('Second.txt', 'w+')
file_to_save.write(str(sorted_dict))
file_to_save.close()
#Второе задание

sorted_by_value_dict = sorted(dict.items(), key=operator.itemgetter(1), reverse=True)

print(sorted_by_value_dict)

file_to_save = open('Third.txt', 'w+')
file_to_save.write(str(sorted_by_value_dict))
file_to_save.close()
#Третье задание

dict_for_gen = {'D': 4, 'A': 1, 'V': 22, 'Y': 25, 'O': 15}

fun_gen = {key: f(int(value)) for key, value in dict_for_gen.items()}

print(fun_gen)
######################
def fun_gen(x):
    y = 1
    for i in range(x):
        if i in (0,1):
            yield 1
        else:
            y = y*i
            yield y
for i in fun_gen(10):
    print(i)

#Четвёртое задание

dict_for_5 = {'D': 4, 'A': 1, 'V': 22, 'Y': 25, 'O': 15}

g = dict_for_5.values()

sred = (sum(g) / len(g)) #Считает среднее арифметическое

dict_for_5_1 = [i for i in g if i < sred]
dict_for_5_2 = [i for i in g if i > sred]

print(dict_for_5_1)
print(dict_for_5_2)

#Пятое задание