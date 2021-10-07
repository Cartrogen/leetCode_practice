import heapq


def reorganise_string(str):
    result = []
    max_heap = []
    frequency_map = {}

    for char in str:
        if char in frequency_map:
            frequency_map[char] += 1
        else:
            frequency_map[char] = 1

    for char, frequency in frequency_map.items():
        heapq.heappush(max_heap, (-frequency, char))

    while max_heap:
        first_count, first_char = heapq.heappop(max_heap)
        result.append(first_char)
        if not max_heap:
            if first_count < -1:
                return "unable to reorganise based on criteria"
            break

        second_count, second_char = heapq.heappop(max_heap)
        result.append(second_char)
        if first_count < -1:
            heapq.heappush(max_heap, (first_count + 1, first_char))
        if second_count < -1:
            heapq.heappush(max_heap, (second_count + 1, second_char))

    result = "".join(result)
    return result


