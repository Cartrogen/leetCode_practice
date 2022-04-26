def maximumSubarray(list):
    maxSum = list[0]
    currentSum = 0
    
    for i in list:

        if (currentSum < 0):
            currentSum = 0

        currentSum += i
        maxSum = max(maxSum, currentSum)
    
    return maxSum

# list = [-2,1,-3,4,-1,2,1,-5,4]
list = [-1]
print(maximumSubarray(list))