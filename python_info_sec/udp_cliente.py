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

porta = 5433

msg = 'boa tarde'

try:
    print('Cliente: ' + msg)
    s.sendto(msg.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: ' + dados)

finally:
    print('Cliente: Fechando a conexão')
    s.close()
