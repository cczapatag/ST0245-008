String = str(input("Ingrese palabra a invertir: "))
def invertir(S):
    if len(S)==1:
        return S
    return S[len(S)-1]+invertir(S[:-1])
print("%s Invertido es %s"%(String,invertir(String)))