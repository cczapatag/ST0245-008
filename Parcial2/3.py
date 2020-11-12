def postorden(preorden, inorden):
    if preorden == "" or inorden == "":
        return ""
    if len(preorden) == 1 or len(inorden) == 1:
        return preorden or inorden
    post = ""
    inorden_izq = ""
    inorden_der = ""
    preorden_izq = ""
    preorden_der = ""
    i = 0
    while inorden[i] != preorden[0]:
        inorden_izq = inorden_izq + inorden[i]
        i += 1
    i += 1
    while i < len(inorden):
        inorden_der = inorden_der + inorden[i]
        i += 1
    i = 0
    for char in preorden:
        if char in inorden_izq:
            preorden_izq = preorden_izq + char
        if char in inorden_der:
            preorden_der = preorden_der + char
    post = post + postorden(preorden_izq, inorden_izq) + postorden(preorden_der, inorden_der) + preorden[0]
    return post

print(postorden("GEAIBMCLDFKJH", "IABEGLDCFMKHJ"))
