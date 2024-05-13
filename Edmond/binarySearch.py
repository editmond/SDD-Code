import randomArray
import randomSearchValue
import sortFuncs

array = randomArray.randomArray()
array = sortFuncs.insertionSort(array)
searchValue = randomSearchValue.randomSearchValue()
lower = 0
upper = len(array) - 1
size = upper - lower
while size > 1:
    #get the "middle" of the array
    middle = int((size)/2) + lower
    print(middle)
    #see which half contains larger values
    if searchValue == array[middle]:
        lower = middle
        upper = lower
    if searchValue < array[middle]:
        upper = middle
    else:
        lower = middle
    size = upper - lower
print(f"Found the value {searchValue} at index: {lower}")