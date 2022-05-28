AB=int(input())
BC=int(input())

AC=((AB**2)+(BC**2))**0.5

import math

MC=AC/2
c=math.asin(MC/BC)
x1=math.degrees(c)

s=str(round(x1))+"\N{DEGREE SIGN}"

print(s)
