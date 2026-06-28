n, k = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()

for i in range(len(nums)):
    if i==k-1:
        print(nums[i])