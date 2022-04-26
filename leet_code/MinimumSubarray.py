def minSubArray(target, numberList):

    minLength = float('inf')
    currSum = 0
    i = 0

    for j in range(len(numberList)):
        currSum = currSum + numberList[j]
        print('sum', currSum)

        while currSum >= target:
            length = j - i + 1
            print(length)
            minLength = min(minLength, length)
            currSum = currSum - numberList[i]
            i += 1

    if minLength == float('inf'):
        return 0
    else:
        return minLength


target = 7
nums = [2, 3, 1, 2, 4, 3]

print(minSubArray(7, nums))
