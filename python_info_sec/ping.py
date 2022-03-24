import os
import pandas as pd
import time as tm

df = pd.read_csv('ip.txt')
print(df['ip'])

#ping_ip = lambda
for ip in df['ip']:
    print('-' * 69)
    print('verificando roust: ' + ip)
    os.system('ping -c 3 {}'.format(ip))
    tm.sleep(2)
