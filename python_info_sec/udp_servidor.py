import socket as sk
import os
import sys


try:
    s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)
except sk.error as e:
    print('A conexão falhou!')
    print('Erro: {}'.format(e))
    sys.exit()

print('Socket criado com sucesso!')

host = 'localhost'

porta = 5432

s.bind((host, porta))

msg = '\n Servidor: boa tarde não. Bom dia'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('servidor enviado mensagem...')
        s.sendto(dados + (msg.encode()), end)
