import socket as sk
import os
import sys


def main():
    try:
        s = sk.socket(sk.AF_INET, sk.SOCK_STREAM, 0)
    except sk.error as e:
        print('A conexão falhou!')
        print('Erro: {}'.format(e))
        sys.exit()

    print('Socket criado com sucesso!')

    hostalvo = input("Digite o host ou ip a ser conectado:")
    portaalvo = input("Digite a porta a ser conectado:")

    try:
        s.connect((hostalvo, int(portaalvo)))
        print('Cliente TCP conectado com sucesso em {} pela porta {}'.format(hostalvo, portaalvo))
        s.shutdown(2)
    except sk.error as e:
        print('Não foi possível conectar em {} pela porta {}'.format(hostalvo, portaalvo))
        print('Erro: {}'.format(e))
        sys.exit()

if __name__ == "__main__":
    main()
