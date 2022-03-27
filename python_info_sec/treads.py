from threading import Thread

def carro1(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('carro1: ', trajeto)
        trajeto += velocidade

def carro2(velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('carro2: ', trajeto)
        trajeto += velocidade

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print('piloto: {}, trajeto {}.\n '.format(piloto, trajeto))
        trajeto += velocidade


t_carro1 = Thread(target = carro, args=[1, 'Bruno'])
t_carro2 = Thread(target = carro, args=[2, 'Lucas'])

t_carro1.start()
t_carro2.start()

#carro1(10)
#carro2(20)