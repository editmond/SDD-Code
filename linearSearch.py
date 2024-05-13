import randomArray
import randomSearchValue

array = randomArray.randomArray()
searchValue = randomSearchValue.randomSearchValue()
i = 0
found = False
index = 0
while i < len(array) and not found:
    if array[i] == searchValue:
        index = i
        found = True
    i += 1
print(f"Searching for: {searchValue}, found at index: {index}")