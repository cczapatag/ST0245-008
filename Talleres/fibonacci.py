n=int(input("Ingrese el numero de iteraciones: "))
def fibonacciR(n):
    if n<=2:
        return 1
    else:
        return fibonacciR(n-1)+fibonacciR(n-2)
print("El valor para la sucesion",n,"es",fibonacciR(n))