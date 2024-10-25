#Endryl Cavalcante Oliveira Goes
soma = 0
valor1=int(input("Digite o valor menor: "))
valor2=int(input("Digite o valor maior: "))

for n in range(valor1, valor2+1):
    soma += n

print(f"A soma de todos os números entre esses dois valores é de: {soma}")