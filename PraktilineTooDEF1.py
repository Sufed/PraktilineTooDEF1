import math
#Harjutus 8.

#Harjutus 7.

#Harjutus 6.
print("Harjutus 6.")
def is_prime(число):
    if число<2:
        return False
    for i in range(2, число):
        if число%i==0:
            return False
    return True
#Harjutus 5.
print("Harjutus 5.")
a=float(input("Сумма вклада: "))
лет=int(input("На сколько лет вклад? "))
def bank(a, лет):
    for i in range(лет):
        a=a+a*0.1
    return a
результат=bank(a, лет)
print(результат)
#Harjutus 4.
print("Harjutus 4.")
месяц=int(input("Введи месяц по счету: "))
def сезон(месяц):
    if месяц in [3, 4, 5]:
        return "Весна"
    elif месяц in [6, 7, 8]:
        return "Лето"
    elif месяц in [12, 1, 2]:
        return "Зима"
    else:
        return "Осень"
результат=сезон(месяц)
print(результат)
#Harjutus 3.
print("Harjutus 3.")
сторона=float(input("Введи длинну стороны: "))
def квадрат(сторона):
    периметр=4*сторона
    площадь=сторона**2
    диагональ=math.sqrt(2)*сторона #math.sqrt вычисляет квадратный корень числа.
    return периметр, площадь, диагональ
результат=квадрат(сторона)
print(результат)
#Harjutus 2.
print("Harjutus 2.")
год=2023
def высокосный(год): #%-находит остаток.
    if год%4==0:
        if год%100==0:
            if год%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
результат=высокосный(год)
print(результат)
#Harjutus 1.
print("Harjutus 1.")
a=float(input("Введите первую цифру: "))
b=float(input("Введите вторую цифру: "))
operation = input("Введите операцию (+, -, *, /): ")
def arithmetic(a, b, operation):
    if operation=='+':
        return a+b
    elif operation=='-':
        return a-b
    elif operation=='*':
        return a*b
    elif operation=='/':
        return a/b
    else:
        return "Неизвестная операция"
результат=arithmetic(a, b, operation)
print("Результат:", результат)


