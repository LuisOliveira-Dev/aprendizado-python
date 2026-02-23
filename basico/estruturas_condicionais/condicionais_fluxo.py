#if -> funciona sozinho
#else -> contrário de if
#elif -> vem antes do else
#else e elif -> não podem estar sozinhos
condicao1 = False
condicao2 = False
condicao3 = True
condicao4 = False

if condicao1:
    print('Código para condição 1')
elif condicao2:
    print('Código para condição 2')
elif condicao3:
    print('Código para condição 3')
elif condicao4:
    print('Código para condição 4')
else:
    print('Nenhuma condição foi satisfeita')

