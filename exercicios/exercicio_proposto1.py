'''
Exercício
Seu nome é {nome}
Seu nome invertido é {nome invertido}
seu nome tem {n} letras
A primeira letra do seu nome é {letra}
A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: exiba 'Desculpe, você deixou os campos vazios'
'''

nome1 = input('Nome: ')
idade = input('Digite sua idade: ')

if not nome1 or not idade:
    print('Desculpe, você deixou os campos vazios')
    exit()

print(f'{nome1[::-1]}')
print(len(nome1))
print(nome1[0])
print(nome1[-1])



