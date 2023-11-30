class Standing:
    def __init__(self):
        print("initialized")

    def qoEf(self, pwf, pr, qo, ef):
        # 3 Realizar calculos para la curva ipr
        if ef == 1:
            qoEf = qo * (1 - 0.2 * (pwf / pr) - 0.8 * pow((pwf / pr), 2))
        elif ef < 1:
            # 3 Realizar calculos para la curva ipr
            # qoEf gasto
            qoEf = qo * (
                1.8 * ef * (1 - (pwf / pr)) - 0.8 * pow(ef, 2) * pow(1 - (pwf / pr), 2)
            )
        elif ef > 1:
            # 3 Realizar calculos para la curva ipr
            qoEf = qo * (
                1.8 * ef * (1 - (pwf / pr)) - 0.8 * pow(ef, 2) * pow(1 - (pwf / pr), 2)
            )
        return qoEf

    def standing(self, pwf, pr, qo, ef, n):
        # Presion de fondo fluyente con dano =1
        pwfs = round(pr - (pr - pwf) * ef,3)

        # Paso 1 Calcular el gasto máximo
        qoMaxEf1 = round((qo) / (1 - 0.2 * (pwfs / pr) - 0.8 * pow(pwfs / pr, 2)),3)

        # 2. Calcular el gasto máximo a la eficiencia de flujo deseada
        if ef < 1:
            qoMaxEfD = round(qoMaxEf1 * (1.8 * ef - 0.8 * pow(ef, 2)),3)
        elif ef > 1:
            qoMaxEfD = round(qoMaxEf1 * (0.624 + 0.376 * ef),3)

        # 3 Realizar proceso para retorno de array para grafica
        lpwf = [pr]
        for i in range(1, n + 1):
            aux = round((pr - 14.7) / n, 3)
            lpwf.append(round(pr - (aux * i), 3))  # Metodo para agregar datos de pwf
            if i == n:
                lpwf.append(0)
        lqoEf = list()
        lqoEf1 = list()
        for i in lpwf:
            lqoEf.append(round(self.qoEf(i, pr, qoMaxEf1, ef), 3))
            lqoEf1.append(round(self.qoEf(i, pr, qoMaxEf1, 1), 3))

        return {
            "pwfs": pwfs,
            "qoMaxEf1": qoMaxEf1,
            "qoMaxEfD": qoMaxEfD,
            "lpwf": lpwf,
            "lqoEf": lqoEf,
            "lqoEf1": lqoEf1,
        }
