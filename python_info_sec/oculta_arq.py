import ctypes as ct

atributo_ocultar = 0x02

retorno = ct.windll.kernel32.SetFileAttributesW('a.txt', 'atributo_ocultar') 
if retorno:
    print('arquivo foi ocultado')
else:
    print('arquivo não foi ocultado')