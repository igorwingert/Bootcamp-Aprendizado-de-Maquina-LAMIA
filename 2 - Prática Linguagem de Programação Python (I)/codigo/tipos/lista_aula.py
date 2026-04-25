nums = [1, 2, 3]
print(type(nums))  # list

nums.append(3)
nums.append(4)
nums.append(500)
print(len(nums))

print(2 in nums)  # true

nums[3] = 100  # index 3 vira 100
nums.insert(0, -200)  # add -200 no começo

print(nums[6])
print(nums[-1])
print(nums[-2])

print(nums)
