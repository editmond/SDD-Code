import randomArray

values = randomArray.randomArray()
original = values.copy()
sortedIndex = len(values)

for i in range(len(values)):
    print(f"{values[i]}")
    largestIndex = 0
    for j in range(sortedIndex):
        if values[j] >= values[largestIndex]:
            largestIndex = j
    temp = values[sortedIndex-1]
    x = values[largestIndex]
    values[sortedIndex-1]= x
    values[largestIndex] = temp
    print(values)
    sortedIndex -= 1

print(original)
print(values)