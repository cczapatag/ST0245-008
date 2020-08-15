def torresDeHanoi(n,Tinicio='1',Tintermedio='2',Tfin='3'):
    if n>0:
        torresDeHanoi(n-1,Tinicio,Tfin,Tintermedio)
        print ("Se mueve el anillo:",n,"de la torre",Tinicio,"a la torre",Tfin)
        torresDeHanoi(n-1,Tintermedio,Tinicio,Tfin)
n=int(input("Ingrese el numero de anillos: "))
torresDeHanoi(n)
movimientos=pow(2,n)-1
print("Se han realizado",movimientos,"movimientos")