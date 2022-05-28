n=int(input())
import string
x=string.ascii_lowercase
for i in range(n):
    print("-"*2*(n-i+1))

for j in range(n-1):
    print("-"*2*(j+1))


