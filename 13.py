
from ipaddress import *
# Адрес маски обязателен

# ---------------------------------------------------------------------------

#net = ip_network('218.194.82.148/255.255.255.192', 0)
# при переборе адресов циклом крайние адреса являются адресом сети и широковещательным адресом, не учитываем под юзера.
# net.hosts() выведет все, кроме них
# когда речь про все адреса сети, то hosts() не используем

# ---------------------------------------------------------------------------

#k = 0
#net = ip_network('5.2.5.0/255.255.0.0', 0)
#for ip in net:
#   ip_binary = (bin(int(ip))[2:].zfill(32))
#   if ip_binary.count('0') % 25 == 0:
#      k += 1
#print(k)

# ---------------------------------------------------------------------------

#k = 0
#net = ip_network('112.160.0.0/255.240.0.0',0)
#for ip in net:
#   ip_binary = (bin(int(ip))[2:].zfill(32))
#   if ip_binary.count('1') % 5 == 0:
#      k += 1
#print(k)

# ---------------------------------------------------------------------------

# Маску можно задать, если не дана в задаче

# 218(1-ый байт маски).48(2-й байт маски).192(3-й байт маски).56(4-ый байт маски)

#for m in range(0,33):
#   net = ip_network(f'218.48.192.56/{m}',0) # адрес узла
#    if str(net.network_address) == '218.48.192.0':
#        if len(list(net.hosts())) > 500: # берем только адреса узлов, list из-за сложности объекта
#            print(net.netmask)
#6

# ---------------------------------------------------------------------------

# for m in range (0,33) - КОЛ-ВО ЕДИНИЦ В МАСКЕ
# Для маски пишем f в начале и {m} в конце

#for m in range(0,33):
#    net1 = ip_network(f'157.127.172.56/{m}',0)
#    net2 = ip_network(f'157.127.191.78/{m}',0)
#    if str(net1.network_address) != str(net2.network_address):
#        print(m) # ищем наименьшее возможное кол-во единиц в маске
#20

# ---------------------------------------------------------------------------

#for A in range(0,255): # 0,255 т.к перебираем БАЙТ узла
#    net = ip_network(f'116.242.{A}.26/255.255.255.224',0)
#    usl = [bin(int(ip))[2:].zfill(32)[:16].count('1') >= bin(int(ip))[2:].zfill(32)[16:].count('1') for ip in net]
#    if all(usl):
#        print(A)

# ---------------------------------------------------------------------------

for m in range(0,33):
    net1 = ip_network(f'216.54.187.235/{m}',0)
    net2 = ip_network(f'216.54.174.128/{m}',0)
    if str(net1.network_address) != str(net2.network_address): # проверка на разности адресов сетей
        if '216.54.187.235' != str(net1.network_address) and '216.54.187.235' != str(net1.broadcast_address):
            if '216.54.174.128' != str(net2.network_address) and '216.54.174.128' != str(net2.broadcast_address):
                # проверка на то, что данный нам адрес не является адресом сети и широковещательным узлом.
             print(m)



