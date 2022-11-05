# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

import random

k = int(input('Введите число от 1 до 9: '))
list = [0]*(k+1)
for i in range(len(list)):
    list[i] = str(random.randint(0,101)) +'x^'+str(k) +' + '
    if k == 1:
        list[i] = str(random.randint(0,101))+'x + '
    if k == 0:
        list[i] = str(random.randint(0,101))+' = 0'
    k-=1
print(''.join(list))

data = open('file.txt','w')
data.writelines(list)
data.close