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
