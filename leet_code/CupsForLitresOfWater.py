def cups_for_litres_of_water(N, K):

    if N > K:
        return 1

    capacity = []
    for num in range(1, N+1):
        capacity.append(num)

    i = len(capacity) - 1
    remainder = K
    cups = 0

    while i >= 0 and remainder != 0:
        if remainder in capacity:
            cups += 1
            return cups
        else:
            remainder = remainder - capacity[i]
            capacity.pop()
            cups += 1
            i -= 1

    if remainder == 0:
        return cups

    return -1
