import hashlib as hs

arq1 = 'a.txt'
arq2 = 'b.txt'

hash1 = hs.new('ripemd160')

hash1.update(open(arq1, 'rb').read())

hash2 = hs.new('ripemd160')

hash2.update(open(arq2, 'rb').read())
print(hash1.digest())
print(hash2.digest())

if hash1.digest() != hash2.digest():
    print('O arquivo {} é diferente do arquivo {}.'.format(arq1,arq2))
    
else:
    print('O arquivo {} é igual do arquivo {}.'.format(arq1,arq2))