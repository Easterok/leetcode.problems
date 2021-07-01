# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def fn(nums, target):
  for i in range(len(nums)):
    for k in range(i, len(nums)):
      if nums[i] + nums[k] == target:
        return [i, k]
  
  return []

print(fn([2, 7, 11, 15], 9))

