class Eickmeier:
    def __init__(self):
        print("Initializing")

        # Paso 1 De una prueba de producción, con la ecuación de Vogel, determinar qo(max)Presente

    def qomaxP(self, qoP, pwf, prP):
        return qoP / (1 - 0.2 * (pwf / prP) - 0.8 * pow((pwf / prP), 2))

    # Este metodo calcula el gasto maximo presente

    # Paso 2 Para determinar qo(max)Futura utilizar qo(max)Presente
    def qomaxF(self, prF, prP, qomP):
        return qomP * pow((prF / prP), 3)

    # Este metodo calcula el gasto maximo futuro

    def qo(self, fqomaxF, pwf, prF):
        return round(fqomaxF * (1 - 0.2 * (pwf / prF) - 0.8 * pow((pwf / prF), 2)), 3)

    # Paso 3 Para determinar qo Futura
    def eickmeier(self, qoP, prP, pwfP, pwfF, prF, n):
        fqomaxP = round(self.qomaxP(qoP, pwfP, prP), 3)
        fqomaxF = round(self.qomaxF(prF, prP, fqomaxP), 3)
        fqoF = self.qo(fqomaxF, pwfF, prF)
        print(f"qomaxP= {fqomaxP}\nqomaxF= {fqomaxF}\nqoF= {fqoF}")
        lpwfP = list(prP - i * (prP / n) for i in range(0, n))
        lpwfF = list(prF - i * (prF / n) for i in range(0, n))
        lpwfP.append(0)
        lpwfF.append(0)
        lqoP = list(self.qo(fqomaxP, pwf, prP) for pwf in lpwfP)
        lqoF = list(self.qo(fqomaxF, pwf, prF) for pwf in lpwfF)

        return {
            "qoMaxP": fqomaxP,
            "qoMaxF": fqomaxF,
            "qoF": fqoF,
            "lpwfP": lpwfP,
            "lpwfF": lpwfF,
            "lqoP": lqoP,
            "lqoF": lqoF 
        }
