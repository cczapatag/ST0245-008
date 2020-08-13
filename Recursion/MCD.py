m=int(input("Ingrese el valor mayor"))
n=int(input("Ingrese el valor menor"))
def MCD (n,m):
    if m%n == 0:
        return n
    else:
        return MCD(m,n%m)
print("El MCD de", n, "y", m, "es", MCD(n,m))
