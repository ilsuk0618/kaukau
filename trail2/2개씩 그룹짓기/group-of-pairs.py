n = int(input())
nums = list(map(int, input().split()))
max_val=0
nums.sort()

for i in range(len(nums)//2):
    if max_val<=(nums[i]+nums[len(nums)-i-1]):

        max_val=(nums[i]+nums[len(nums)-i-1])

print(max_val)