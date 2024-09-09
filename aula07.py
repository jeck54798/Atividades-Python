#Tabuada
con = 0
num = int(input("Escreva o número que desaja ver a tabuada: "))
while (con <= 10):
    resultado = num * con
    print(f"{num} X {con} = {resultado}")
    con+=1

#loop while
con = 1
fat = 1
num = int(input("Escreva um número que deseje ver o fatorial: "))
while(con <= num):
    fat*=con #fatorial = fatorial * contador
    con+=1
print(f"O fatorial de {num} é {fat}")

#numeros pares
con = 2
num = int(input("Escreva o número que queira saber a soma dos numeros pares antes dele: "))
par = 0
while(con <= num):
    par = par + con
    con+=2
print(par)

