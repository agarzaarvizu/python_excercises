def calcula_calificacion(score):
    if score >= 0 and score <= 1:
        if score >= 0.9:
            score_text = "Sobresaliente"
        elif score >= 0.8 and score < 0.9:
            score_text = "Notable"
        elif score >= 0.7 and score < 0.8:
            score_text = "Bien"
        elif score >= 0.6 and score < 0.7:
            score_text = "Suficiente"
        else:
            score_text = "Insuficiente"
    else:
        score_text = "Puntacion Incorrecta"
    return score_text

try:
    score = float(input("Introduzca puntuacion: "))
    score_text = calcula_calificacion(score)
    print(score_text)
except:
    print("Puntacion Incorrecta")
