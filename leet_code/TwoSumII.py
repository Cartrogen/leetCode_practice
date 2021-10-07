def two_sum_II(nums, target):
    l = 0
    r = len(nums) - 1
    result = []

    while l < r:
        if nums[l] + nums[r] < target:
            l += 1
        if nums[l] + nums[r] > target:
            r -= 1
        else:
            result.append(nums[l])
            result.append(nums[r])
            return result
