class Vogel:
    def VogelCaseA(self, qo, pr, pwf, pb, r):
        # Paso 1: obtener el IP
        J = qo / (pr - pwf)
        # print(f'IP = {round(J,3)}')
        # Paso 2: calcular el gasto a la presión de saturación
        qb = J * (pr - pb)
        # print(f'qb = {round(qb,3)}')
        # Paso 3: calcular qc
        qc = (qb * pb) / (1.8 * (pr - pb))
        # print(f'qc = {round(qc,3)}')
        # Paso 4: graficar IPR
        # print(int(pwf / r))
        # la "l" inicial significa que es una lista
        lpwf = [pwf - i for i in range(0, int(pwf), int(pwf / r))]
        lqos, lqob = dict(), dict()
        for i in lpwf:
            if i >= pb:
                lqob[i] = J * (pr - i)
            else:
                lqos[i] = round(
                    qc
                    * (1.8 * (pr / pb) - 0.8 - 0.2 * (i / pb) - 0.8 * pow((i / pb), 2)),
                    3,
                )
        lqos[0] = round(qc * (1.8 * (pr / pb) - 0.8), 3)
        return {"J": J, "qb": qb, "qc": qc, "lpwf": lpwf, "lqos": lqos}

    def VogelCaseB(self, qo, pr, pwf, pb, r):
        # Paso 1 Calcular el valor de qc
        qc = qo / (1.8 * (pr / pb) - 0.8 - 0.2 * (pwf / pb) - 0.8 * pow((pwf / pb), 2))
        # print(f'qc = {qc}')
        # Paso 3 Calcular el gasto a la presión de burbuja
        qb = (qc * 1.8 * (pr - pb)) / pb
        # print(f'qb = {qb}')
        # Paso4 Determinar el índice de productividad4.Determinar el índice de productividad
        J = qb / (pr - pb)
        # print(f'IP = {J}')
        # Paso 2 Calcular el gasto para cualquier presión de fondo fluyente por debajo de la presión de burbuja
        # print(int(pwf / r))
        # la "l" inicial significa que es una lista
        lpwf = [pwf - i for i in range(0, int(pwf), int(pwf / r))]
        lqos, lqob = dict(), dict()
        for i in lpwf:
            if i >= pb:
                lqob[i] = J * (pr - i)
            else:
                lqos[i] = round(
                    qc
                    * (1.8 * (pr / pb) - 0.8 - 0.2 * (i / pb) - 0.8 * pow((i / pb), 2)),
                    3,
                )
        lqos[0] = round(qc * (1.8 * (pr / pb) - 0.8), 3)
        return {"qc": qc, "qb": qb, "J": J, "lpwf": lpwf, "lqos": lqos}
