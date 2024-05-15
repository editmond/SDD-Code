num = int(input("number: "))
result = 1
# for n in range(num,0,-1):
#     result = result * n
for i in range(1,num+1):
    print(i)
    result = result * i
print(result)
