#Crie uma lista de 5 números inteiros fornecidos pelo usuário e imprima o maior, o menor e a soma de todos os elementos.

n1=int(input("forneça o primeiro número: "))
n2=int(input("forneça o segundo número: "))
n3=int(input("forneça o terceiro número: "))
n4=int(input("forneça o quarto número: "))
n5=int(input("forneça o quinto número: "))

if n1 > n2 and n3 and n4 and n5:
    print(f"o maior número é {n1}")
elif n2 > n1 and n3 and n4 and n5:
    print(f"o maior número é {n2}")
elif n3 > n2 and n1 and n4 and n5:
    print(f"o maior número é {n3}")
elif n4 > n2 and n3 and n1 and n5:
    print(f"o maior número é {n4}")
elif n5 > n2 and n3 and n4 and n1:
    print(f"o maior número é {n5}")

if n1 < n2 and n3 and n4 and n5:
    print(f"o menor número é {n1}")
elif n2 < n1 and n3 and n4 and n5:
    print(f"o menor número é {n2}")
elif n3 < n2 and n1 and n4 and n5:
    print(f"o menor número é {n3}")
elif n4 < n2 and n3 and n1 and n5:
    print(f"o menor número é {n4}")
elif n5 < n2 and n3 and n4 and n1:
    print(f"o menor número é {n5}")
else:
    print("todos os números são iguais")

SomaValores=n1+n2+n3+n4+n5
print(f"a soma de todos os números é {SomaValores}")