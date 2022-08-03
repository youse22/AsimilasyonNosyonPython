l='0,1,2,3,4,5,6,7,8,9,,22,18,34,56,78'
j=[]
for i in l:
    if index[i%3]==0:
        j.append(i)
print(j)

