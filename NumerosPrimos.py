__author__ = 'Stévillis Sousa'

'''
Peça para que o usuário digite um número inteiro maior do que 1. Se o número for maior do que 1, armazene esse valor em um vetor. 
Peça por um novo número e assim sucessivamente até que o usuário digite 0. Quando isso acontecer, pare de pedir por novos números. 
Mostre na tela quais dos números que ficaram salvos no vetor são primos. Para determiná-los, utilize uma função chamada 
determinar_primo.
'''

def determinar_primo(numero):  
    divisores = 0
    if numero > 0:
        for divisor in range(1, numero):
            if numero % divisor == 0:
                divisores += 1
                if divisores > 1:            
                    break

        if divisores > 1 : # Número não é primo
            return False
        else: # Número é primo
            return numero
    else:
        return None
    
num = int(input('Digite um inteiro maior que 1: '))
lista_numeros = []
while num != 0:
    if num > 1:
        lista_numeros.append(num)
    num = int(input('Digite um inteiro maior que 1: '))

if len(lista_numeros) > 0:    
    print('Os números primos são: ', end=' ')
    conta_primos = 0
    for n in lista_numeros:
        num_primo = determinar_primo(n)
        if num_primo:
            print(num_primo, end=' ')
            conta_primos += 1
    if conta_primos == 0:
        print('Nenhum dos números é primo')    
else:
    print('Nenhum dos números é primo')
