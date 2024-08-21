cond01 = False
cond02 = True
cond03 = True

if (cond01):
    print("Primeira condição verdadeira")
    print("Dentro do If")
elif (cond02):
    print("Segunda condição verdadeira")
    if(True):
        print("Print dentro do segundo If na segunda condição")
elif (cond03):
    print("Terceira condição verdadeira")
else:
    print("nenhuma das condições foi verdadeira")
print("Print fora do else")



cond01 = True

if(cond01):
    print("A condição 1 é verdadeira")
    print("Dentro do If")
else:
    print("A condição 1 é falsa")
print("Fora do IF")