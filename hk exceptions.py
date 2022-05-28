import re

S = input()
if re.search(".[a-zA-Z]",S)==None:
    print(str(S))
else:
    print("Bad String")
    
