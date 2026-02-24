# Exercício:
# Crie um programa que peça ao usuário dois números.
# Em seguida, compare os valores informados.
# Se o primeiro número for maior que o segundo, exiba:
# "Primeiro valor maior".
# Caso contrário, exiba:
# "Segundo valor maior".
#
# Utilize estrutura condicional (if e else) para resolver o exercício.

primeiro_valor = int(input('Primeiro número: '))
segundo_valor = int(input('Segundo número: '))

if primeiro_valor > segundo_valor:
    print('Primeiro valor maior')
else:
    print('Segundo valor maior')