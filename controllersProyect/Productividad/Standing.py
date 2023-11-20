class Standing:
    def __init__(self):
        print("initialized")

    def defaultMethod(self, qoP, prP, pwf, prF, kroP, kroF, vizP, vizF, BoP, BoF, r):
        # Paso 1 calculo de qoMax Presente
        qoMaxP = round(qoP / (1 - 0.2 * (pwf / prP) - 0.8 * pow((pwf / prP), 2)),3)
        # Gasto Max Presnete

        # Paso 2 Usar las propiedades de los fluidos, para calcular IPR presente y futuro
        JF = round((kroF) / (vizF * BoF),3)  # viz es la vizcosidad
        # # IPR Futuro

        JP = round((kroP) / (vizP * BoP),3)  # IPR Presente

        # Paso 3 Calcular 𝑞𝑜(max)𝐹
        qoMaxF = round(qoMaxP * ((prF * JF) / (prP * JP)),3)
        # # Gasto Max Futuro

        # Paso 4 Preparar elementos para la grafica
        # l Representa que sera una lista
        lpwfP = list(round((prP - (prP / r) * i), 3) for i in range(1, r + 1))
        # # Lista de presiones Presente

        lpwfF = list(round((prF - (prF / r) * i), 3) for i in range(1, r + 1))
        # # Lista de presiones futura

        lqoP = list(
            round(qoMaxP * (1 - 0.2 * (pwf / prP) - 0.8 * pow((pwf / prP), 2)), 3)
            for pwf in lpwfP
        )
        # # Lista de Gastos Presente

        lqoF = list(
            round(qoMaxF * (1 - 0.2 * (pwf / prF) - 0.8 * pow((pwf / prF), 2)), 3)
            for pwf in lpwfF
        )
        # # Lista de Gastos Futuras

        return {
            "JF": JF,
            "JP": JP,
            "qoMaxP": qoMaxP,
            "qoMaxF": qoMaxF,
            "lpwfP": lpwfP,
            "lpwfF": lpwfF,
            "lqoP": lqoP,
            "lqoF": lqoF,
        }
