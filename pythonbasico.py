
#essa declaração de variáveis contém principios de atribuição, sendo essas: int, float & operadores l

nome = 'Luis Henrique'
sobrenome = 'Oliveira da Silva'
idade = 19
ano_nascimento = 2005
maior_de_idade = idade > 18
altura_em_metros = 1.80

#essas variáveis contém uma operação matemática com principios de operadores aritméticos

conta_1 = (1 + 1) ** (5 + 5) #'1024'
conta_2 = 1 + 1 ** 5 + 5 #'7'

"""
Cálculo IMC : IMC = peso / altura ** 2

Argumentos:
    peso (float): Peso em quilogramas.
    altura(float): Altura em metros.

Retorno: 
    float: Valor do IMC.
"""
altura = 1.80
peso = 65
imc = peso / (altura ** 2)
imc = round(imc, 2)

#input: lê dados de acordo com o usuário

nome_2 = input('Digite seu nome:')
numero = input('Digite um número:')

#váriavel pra estrutura condicional

entrada = input('"entrada" ou "sair"?')

#Print referente as variaveis de int, float e operadores lógicos 

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano nascimento:', ano_nascimento)
print('Maior de idade:', maior_de_idade)
print('Altura em metros: {:.2f}'.format(altura_em_metros))

print(' ')

#Print referente a variável de operadores aritméticos 

print('Resultado:',conta_1)
print('Resultado:',conta_2)

print(' ')

#Print referente ao imc

print('IMC:', imc)

#Print referente ao input

print(f'Nome_2: {nome_2}')
print(f'Número: {numero}')

"""
Estruturas condicionais:
if: se
elif: se não se
else: se não
"""

if entrada == 'entrada':
    print('você entrou no sistema')
elif entrada == 'sair':
    print('você saiu do sistema')
else:
    print('Você não digitou entrada nem saída.')





