def triangulo(base1,base2):
    if(base1==base2 or base2==0):
        return 1
    else:
        return (triangulo(base1-1,base2-1)+triangulo(base1-1, base2))
n=int(input("Ingrese la cantidad de lineas de la piramide a mostrar: "))
for i in range(n):
    for j in range(i+1):
        print(" ", triangulo(i,j)," ", end="")
    print("")