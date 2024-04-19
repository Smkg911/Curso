class Curso: 
    '''-------------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------------'''
    def __init__(self):
        self.__notas = [4.0,2.0,4.6,3.1,2.7,4.2,0.5,1.6,0.8,1.9,5.0,4.1]

    # def promedioBien(self): 
    #     return (sum(self.__notas)/len(self.__notas))
    
    # def promedio(self):
    #     nota1, nota2, nota3, nota4, nota5, nota6, nota7, nota8, nota9, nota10, nota11, nota12 = self.__notas
    #     __notas = nota1 + nota2 + nota3 + nota4 + nota5 + nota6 + nota7 + nota8 + nota9 + nota10 + nota11 + nota12
    #     return __notas / 12
    
    def calcularPromedio(self):
        promedio = 0
        indice = 0
        while indice < 12:
            promedio += self.__notas[indice]
            indice += 1
        return promedio / indice 
    
    def numeroAprobados(self): 
        numeroAprobados = 0
        indice = 0
        while indice < 12: 
            if self.__notas[indice] >= 3.0 and self.__notas[indice]<= 5:
                numeroAprobados += 1
            indice +=1
        return numeroAprobados
    
    def cambiarNota(self,numeroEstudiante,nNota):
        self.__notas[numeroEstudiante] = nNota

    def calcularCantidadAprobados2(self):
        aprobados = 0
        for indice in range(12):
            if self.__notas[indice] >= 3.0 and self.__notas[indice]<= 5.0:
                aprobados += 1
        return aprobados
    
    def CalcularCantidadAprobados3(self):
        aprobados = 0

        for nota in self.__notas:
            if nota >= 3.0 and nota >= 5.0:
                aprobados += 1
        return aprobados 
    
    def calcularMayorNota(self):
        notaMayor = 0
        for nota in self.__notas:
            if nota >= notaMayor:
                notaMayor = nota 
        return notaMayor
    
    # aumenta un 5% a todas las notas sin sobrepasar el 5 
    def hacerCurva(self):
        for indice in range(12):
            if ((self.__notas[indice]*0.05)+self.__notas[indice]) <= 5.0:
                self.__notas[indice] = self.__notas[indice] + (self.__notas[indice] *0.05)

    def cambiarNotas(self):
        for indice in range(12):
            if self.__notas[indice] > 4.0: 
                self.__notas[indice] -= 0.5
            elif self.__notas[indice] < 2.0: 
                self.__notas[indice] += 0.5
    
    def calcularMayorNota(self):
        notaMenor = 5.0
        for nota in self.__notas:
            if nota <= notaMenor:
                notaMenor = nota 
        return notaMenor

    def darRangoConMasNotas(self):
        rango1 = 0
        rango2 = 0
        rango3 = 0
        
        for nota in self.__notas:
            if nota >= 0.0 and nota <= 1.99:
                rango1 += 1
            elif nota >= 2.0 and nota <= 3.49:
                rango2 += 1
            elif nota >= 3.5 and nota <= 5.0:
                rango3 +=1

        if rango1 > rango2 and rango1 > rango3:
            return f"rango1 con {rango1} notas"
        elif rango2 > rango1 and rango2 > rango3:
            return f"rango2 con {rango2} notas"
        elif rango3 > rango2 and rango3 > rango1:
            return f"rango3 con {rango3} notas"


