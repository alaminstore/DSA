
numbers = [20,14,56,22,57,85,35,33,57,54,22,77,42]
def binarySearch(numbers,search_number,low,high):
  numbers.sort()
  print(numbers)
  while low <= high:
    mid = low + (high-low)//2
    if(search_number == numbers[mid]):
      return mid
    elif(search_number > numbers[mid]):
      low = mid+1
    else:
      high = mid-1    
  return -1

result = binarySearch(numbers,42,0,len(numbers)-1)
if result != -1:
  print('Index of the search number is:' + str(result))
else:
  print('Not Found')