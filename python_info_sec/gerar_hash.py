import hashlib as hs
import sys
string = input("Digite o texto de referência:")
r_str = ''
encode_menu = int(input('''Escolha o tipo de encode:
                        1) MD5;
                        2) SHA1;
                        3) SHA256
                        4) SHA512
                    Valores diferentes encerrarão o programa: '''))


if encode_menu == 1:
    resultado = hs.md5(string.encode('utf-8'))
    cd = 'MD5'
elif encode_menu == 2:
    resultado = hs.sha1(string.encode('utf-8'))
    cd = 'SHA1'
elif encode_menu == 3:
    resultado = hs.sha256(string.encode('utf-8'))
    cd = 'SHA256'
elif encode_menu == 4:
    resultado = hs.sha512(string.encode('utf-8'))
    cd = 'SHA512'
else:
    print('Não foi informada uma opção válida. A aplicação será encerrada.')
    sys.exit()

r_str = str(resultado)
#print('o resultado da string é: ', resultado.hexdigest())

print('Para o encode {} o resultado é {} com {} caractéres '.format(cd,resultado.hexdigest(),len(resultado.hexdigest())))
