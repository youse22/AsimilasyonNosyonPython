k="Ayiti pap peri a"
k=k.lower()
j=[]
for i in range(len(k)):
    if k[i]=="a":
        c=i
        j.append(c)
print(sum(j))