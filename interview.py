# Hi, here's your problem today. This problem was recently asked by Facebook:

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

solution:
nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
def moveZeros(nums):
  for num in range(len(nums)-1):
      if(nums[num] == 0):
          nums.append(0)
          nums.remove(nums[num])
  return nums
result = moveZeros(nums)
print(result)

