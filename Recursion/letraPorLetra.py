cadena = str(input("Ingrese una palabra: "))
iterador = 1
def letraporletra(string, iterador):
    print(cadena[0:iterador])
    if iterador != len(cadena):
       letraporletra(string, iterador+1)
letraporletra(cadena, iterador)