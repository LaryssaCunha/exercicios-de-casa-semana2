# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
    
print("Programa de uma escola. A nota final de cada bimestre da escola é composta por nota de trabalho, nota de participação e nota da prova. O mínimo para ser aprovado é de 21. O programa vai calcular as notas para obter o total e dizer se foi aprovado ou não.")

nota1 = int(input("Digite aqui a nota do trabalho: "))
nota2 = int(input("Digite aqui a nota de participação: "))
nota3 = int(input("Digite aqui a nota da prova: "))

def calcular_nota_mensal(nota1, nota2, nota3):
    nota_mensal = nota1 + nota2 + nota3
    print(nota_mensal)
    return(nota_mensal)

nota_mensal = calcular_nota_mensal(nota1, nota2, nota3)

if nota_mensal > 20:
    print("A aluna está aprovada.")
else:
    print("A aluna está reprovada.")