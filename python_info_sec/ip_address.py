import ipaddress as ipa

ip = '192.168.0.1'
ipr = ip + '/24'


endereco = ipa.ip_address(ip)

rede = ipa.ip_network(ipr, strict = False)

print(endereco + 500)

for i in rede:
    print(i)