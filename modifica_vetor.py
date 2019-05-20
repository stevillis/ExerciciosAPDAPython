__author__ = 'Stévillis Sousa'

'''
Faça um algoritmo que solicite ao usuário números e os armazene em um vetor de 20 posições. Crie uma função que receba o vetor 
preenchido e substitua todas as ocorrências de valores negativos por 0, as de valores menores do que 10 por 1 e as demais por 2.
'''

cont = 0
vetor = []

def modifica_vetor(vetor):
    for cont, num in enumerate(vetor):        
        if num < 0:            
            vetor[cont] = 0
        elif num < 10:
            vetor[cont] = 1
        else:
            vetor[cont] = 2
    return vetor
        
            
while cont < 20:
    num = int(input(f'Digite o {cont+1}º número: '))
    vetor.append(num)
    cont += 1


print(f'Vetor original: {vetor}')
vetor_modificado = modifica_vetor(vetor)
print(f'Vetor modificado: {vetor_modificado}')
