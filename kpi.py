#Desafio - Cálculo de Bônus com Entrada do Usuário
#Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
#o valor do seu salário mensal e o valor do bônus que recebeu. 
#O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor do salário em comparação com o bônus recebido.
#O cálculo do KPI do bônus é 1000 + Salário * Bônus

CONST_BONUS = 1000
nome  = input("Informe o seu nome: ")
sal   = float(input("Informe o seu salário mensal: "))
bonus = float(input("Informe o seu bônus recebido: "))
final = CONST_BONUS + (sal * bonus)

print(f"Olá {nome}, seu bônus foi de {final}")