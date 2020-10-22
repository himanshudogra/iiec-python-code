def Nmaxelements(list,N):
    final_list = [] 
    for i in range(0,N):
        max=0

        for j in range(len(list)):
            if list[j] > max:
                max=list[j]
        list.remove(max)
        final_list.append(max)
    
    print(final_list)



list=[2,4,8,10,50,90,48]
N=2

Nmaxelements(list,N)