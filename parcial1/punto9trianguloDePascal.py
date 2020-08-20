def pascal(row,column):
    if row < 0 and column < 0:
        return 0
    elif(row==column or column==0):
        return 1
    else:
        return (pascal(row-1,column-1)+pascal(row-1, column))
n=int(input("Ingrese la cantidad de lineas de la piramide a mostrar: "))
for i in range(n):
    for j in range(i+1):
        print(" ", pascal(i,j)," ", end="")
    print("")