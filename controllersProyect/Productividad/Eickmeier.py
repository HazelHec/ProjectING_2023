class Eickmeier:
    def __init__(self):
        print ("Initializing")

    def defaultMethod(self,qoP,prP,pwf,prF):
        #Metodos y funciones 
        #Paso 1 De una prueba de producción, con la ecuación de Vogel, determinar qo(max)Presente
        qomaxP = qoP / ( 1 - 0.2 * (pwf/prP) - 0.8 * pow((pwf/prP),2))
        #Este metodo calcula el gasto maximo presente


        #Paso 2 Para determinar qo(max)Futura utilizar qo(max)Presente
        qomaxF = qomaxP * pow((prF/prP),3)
        #Este metodo calcula el gasto maximo futuro

        #Paso 3 Para determinar qo Futura
        qoF = round(qomaxF * (1 - 0.2 * (pwf/prF) - 0.8 * pow((pwf/prF),2)),3)

        return {"qomaxP": qomaxP, "qomaxF": qomaxF, "qoF": qoF}     
        