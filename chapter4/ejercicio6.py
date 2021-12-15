def calculo_salario(hours, cost):
    if hours>40:
        extra_hours = (hours - 40) * (cost * 1.5)
        salary = (cost * 40) + extra_hours
    else:
        salary = cost * hours
    return salary

try:
    hours = int(input("Introduzca las Horas: "))
    cost = float(input("Introduzca la Tarifa por hora: "))
    salary = calculo_salario(hours, cost)
    print("Salario: ", salary)

except:
    print("Error, por favor introduzca un numero")

