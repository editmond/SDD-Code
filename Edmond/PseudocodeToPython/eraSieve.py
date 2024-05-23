def sieveEra(n):
    p = 2
    list = []
    for i in range(2,n):
        list.append(i)
    while p*p <= n:
        for i in range(0,len(list)-1):
            if list[i] % p == 0 and list[i] / p != 1:
                list[i] = 0
        p+=1
    return list

print(sieveEra(11))