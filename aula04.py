#Algoritmo média 

print("Óla, vamos ver a sua média")

nota1=float(input("Digite o valor de sua primeira nota: "))
nota2=float(input("Digite o valor de sua segunda nota: "))
nota3=float(input("Digite o valor de sua terceira nota: "))
nota4=float(input("Digite o valor de sua quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

print("A sua média foi", media)
if(media >= 80):
    print("Parabéns, você foi aprovado")
elif(media >= 60):
    print("Você está de recuperação")
else:
    print("Que pena, você foi reprovado")

print("Continue o bom trabalho")
