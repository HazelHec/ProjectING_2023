import math as mt


class BackPressure:
    def __init__(self):
        print("Initializing")

    def defaultMethod(self, pr, pwf1, pwf2, qg1, qg2, r):
        a = mt.log(pow(pr, 2) - pow(pwf2, 2), 10) - mt.log(
            pow(pr, 2) - pow(pwf1, 2), 10
        )
        b = mt.log(qg2, 10) - mt.log(qg1, 10)
        
        # Calcular m
        m = a / b  # Esta es m

        # Calculo de n
        n = 1 / m

        # Calculo de C
        c = qg1 / pow(pow(pr, 2) - pow(pwf1, 2), n)
        
        # Calculo de qg
        pwf = [pr]
        for i in range(1, r + 1):
            aux = round((pr - 14.7) / r, 3)
            pwf.append(round(pr - (aux * i), 3))  # Metodo para agregar datos de pwf
            if i == r:
                pwf.append(0)
        qg = list()
        aux2 = 0
        for i in pwf:
            qg.append(round(c * pow((pow(pr, 2) - pow(i, 2)), n), 3))
            pwf[aux2] = round(pow(pr, 2) - pow(pwf[aux2], 2), 3)
            aux2 += 1

        return {"m": m, "n": n, "c": c, "lpwf": pwf, "lqg": qg}
