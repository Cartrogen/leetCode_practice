def container_with_most_water(height_list):
    max_area = 0
    l = 0
    r = len(height_list) - 1

    while l < r:
        width = r - l
        if height_list[l] > height_list[r]:
            height = height_list[r]
            r -= 1
        elif height_list[l] < height_list[r]:
            height = height_list[l]
            l += 1
        else:
            height = height_list[l]
            r -= 1

        area = width * height

        if area > max_area:
            max_area = area

    return max_area
