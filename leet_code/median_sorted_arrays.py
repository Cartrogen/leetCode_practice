# def sort_list(array1, array2):
#     i = 0
#     j = 0
#     n = 0
#     median_list = []
#
#     while i < len(array1) and j < len(array2):
#         if array1[i] < array2[j]:
#             median_list.append(array1[i])
#             i += 1
#         elif array2[j] < array1[i]:
#             median_list.append(array2[j])
#             j += 1
#         else:
#             median_list.append(array1[i])
#             median_list.append(array2[j])
#             i += 1
#             j += 1
#
#     print(median_list)
#     mid_point = len(median_list) / 2
#     if mid_point % 2 == 0:
#
#
#
# sort_list([1, 3, 5], [2, 3, 4])
