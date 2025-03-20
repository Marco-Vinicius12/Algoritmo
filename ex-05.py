#05As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.
print("Quantas maças você comprou:")
num = int(input())
valor = 0
print("voce comprou", num,"maças")
if num <= 12:
    valor = 1.3
else:
    valor = 1.0
print("valor total gasto é de R$:",num*valor)
