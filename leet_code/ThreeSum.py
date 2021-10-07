def three_sum(nums):
    result = []
    nums.sort()

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            i += 1

        l = i + 1
        r = len(nums) - 1

        while l < r:
            if nums[i] + nums[l] + nums[r] < 0:
                l += 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            else:
                result.append([nums[i], nums[l], nums[r]])
                l += 1
                if nums[l] == nums[l - 1]:
                    l += 1

    return result
