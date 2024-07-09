import math

def function():
    try:
        Number = int(input("Введите положительную числовую переменную: "));
        Factorial = math.factorial(Number)
        print("Факториал числа", Number, "Равен", Factorial)
    except:
        function()
function()
