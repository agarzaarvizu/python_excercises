try:
    score = float(input("Introduzca puntuacion: "))
    if score >= 0 and score <= 1:
        if score >= 0.9:
            print("Sobresaliente")
        elif score >= 0.8 and score < 0.9:
            print("Notable")
        elif score >= 0.7 and score < 0.8:
            print("Bien")
        elif score >= 0.6 and score < 0.7:
            print("Suficiente")
        else:
            print("Insuficiente")
    else:
        print("Puntacion Incorrecta")
except:
    print("Puntacion Incorrecta")
