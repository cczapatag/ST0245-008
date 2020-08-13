String = str(input("Ingrese palabra a determinar si es palindromo: "))
def palindromo (String):
    if len(String)<1:
        return "R/: Eso es Verdadero"
    else:
        if String[0]==String[-1]:
            return palindromo(String[1:-1])
        else:
            return "R/: Eso es Falso"
print("¿La palabra",String,"es palindromo?",palindromo(String))