hours = int(input("Introduzca las Horas: "))
cost = float(input("Introduzca la Tarifa por hora: "))

if hours>40:
    extra_hours = (hours - 40) * (cost * 1.5)
    salary = (cost * 40) + extra_hours
else:
    salary = cost * hours

print("Salario: ", salary)


