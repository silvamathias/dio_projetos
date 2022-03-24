def teste(nome):
    dic1 = {
        'pedro':43,
        'mario':26,
        'carlos':29,
        'mirian':34}

    idade = dic1[nome]

    dic2 = {'idade': idade, 'nome': nome}
    return dic2

nomes = ['mario', 'pedro', 'mirian']

dn = []
for n in nomes:
    dn += [teste(n)['idade']]

print(dn)
print('-'*77)
teste_lam = lambda lista_nome: [teste(n)['idade'] for n in lista_nome]

print(teste_lam(nomes))
print('-'*77)
procura = 34
if procura in teste_lam(nomes):
    print('ao menos uma pessoa tem {} anos'.format(procura))
else:
    print('não encontramos pessoas com {} anos'.format(procura))
