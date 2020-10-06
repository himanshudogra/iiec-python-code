x=[1,2,3,4,5,6,-1]


m=[i*i if i>0 else 0 for i in x]
j=[i+i for i in x if i!=2]
print(m)
print(j)
