x=int(input("Ingrese la base"))
n=int(input("Ingrese el exponente"))
def potencia(x,n):
    if n==0:
        resultado = 1
    else:
        resultado= x*potencia(x,n-1)
    return resultado
print(potencia(x,n))