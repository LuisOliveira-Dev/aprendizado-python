#and (e)
#se qualquer valor for considerado falso, 
#a expressão inteira será avaliada naquele valor
entrada = input('[E]ntrar [S]air:')
senha_digitada = input('Senha: ')

senha_permitida = '123456'
if entrada == 'E' and senha_digitada == senha_permitida:
    print('entrada')

elif entrada == 'S': 
    print('saida')

else:
    print('Resposta inválida')