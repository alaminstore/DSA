menu = [10,33,12,25,23,22,30,31,11,24]
def bubbleSort(items):
    itemRange = len(items)
    for i in range(itemRange-1):
        for j in range(itemRange-1-i):
            if(items[j] > items[j+1]):
                items[j],items[j+1] = items[j+1], items[j]
    return items
    
result = bubbleSort(menu)
print(result)