def ultimosDosDigitosC_C(n):
    if n<=1:
        print("1",end="")
        return 0
    else:
        print(n,"",end="")
        return 0+ultimosDosDigitosC_C(n-1)
ultimosDosDigitosC_C(11)