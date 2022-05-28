ipv4=r"[0-2][0-5][0-5][.]+"
ipv6=r"^[0-9]+[:][0-9]+[a-z]+[0-9]+[:]+[0-9]+$"
import re
n=int(input())
l1=[]
for i in range(n):
    ip_address=input()
    l1.append(ip_address)

for i in range(n):
    if bool(re.search(ipv4,l1[i]))==True:
        print("IPV4")
    elif bool(re.search(ipv6,l1[i]))==True:
        print("IPV6")
    else:
        print("neither")
