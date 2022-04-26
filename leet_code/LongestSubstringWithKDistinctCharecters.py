def longestSubstringWithKDistinctCharecters(givenStr, k):
    i, j, currLength, maxLength, = 0, 0, 0, 0
    stringDictionary = {}

    while j < len(givenStr):
        if givenStr[j] not in stringDictionary.keys():
            stringDictionary[givenStr[j]] = 1
        else:
            stringDictionary[givenStr[j]] += 1

        while len(stringDictionary) > k:
            stringDictionary[givenStr[i]] -= 1
            if (stringDictionary[givenStr[i]] == 0):
                stringDictionary.pop(givenStr[i])
            i += 1

        currLength = j - i + 1
        maxLength = max(maxLength, currLength)

        j += 1

    return maxLength


givenStr = 'eceba'
k = 2

print(longestSubstringWithKDistinctCharecters(givenStr, k))
