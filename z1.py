# Вычислить число c заданной точностью d при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
d = int(input('Какое количество знаков после запятой: '))

number1 = a//b
c = number1
for i in range(1,d+1):
    a = (a-b*c)*10
    c = a//b
    number2 = c*10**-i
    number1 = number1+number2
    
print(round(number1,d))