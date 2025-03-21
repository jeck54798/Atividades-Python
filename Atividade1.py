#Peça ao usuário papra fornecer as seguintes informações:

nome = input("Qual é o seu nome? ")
idade = int(input("Qual é a sua indade? "))
endereço = input("Em que cidade você mora? ")
profissão = input("Qual é a sua profissão? ")
hobby = input("Você poderia descrever um hobby seu? ")

print("INFORMAÇÕES:")
print(f"Seu nome é {nome}")
print(f"Você tem {idade} anos")
print(f"você mora em {endereço}")
print(f"você trabalha como {profissão}")
print(f"e você passa seu tempo com {hobby}")