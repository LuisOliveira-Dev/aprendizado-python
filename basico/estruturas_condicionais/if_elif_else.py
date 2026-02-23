#estruturas condicionais são estruturas 
#que impõe uma condição a uma sentença de código
#if -> se
#elif -> se não se
#else -> se não

entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair':
    print('você saiu do sistema')
else:
    print('Digitação incorreta')