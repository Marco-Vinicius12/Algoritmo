numero1 = int(input("Informe o Primeiro numero:"))
numero2 = int(input("Informe o Segundo numero:"))
numero3 = int(input("Informe o Terceiro numero:"))

if numero1 > numero2 and numero1 > numero3:
    print("primeiro é maior")
elif numero2 > numero1 and numero2 > numero3:
    print("segundo é maior")
else:
    print("terceiro é maior")
