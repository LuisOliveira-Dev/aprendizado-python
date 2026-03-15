#or(ou) 
#avalia uma condição ou outra, Por Exemplo:
#if (entrada == 'E' or entrada == 'e')
entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('entrada')

elif entrada == 'S': 
    print('saida')

else:
    print('Resposta inválida')