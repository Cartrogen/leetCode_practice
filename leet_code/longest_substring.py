# def longest_string(test_string):
#     longest_number = 0
#     longest_string_list = []
#     i = 0
#     j = 0
#     length_string = len(test_string)
#     while i < length_string and j < length_string:
#         if test_string[j] not in longest_string_list:
#             longest_string_list.append(test_string[j])
#             j += 1
#             if len(longest_string_list) > longest_number:
#                 longest_number = len(longest_string_list)
#         else:
#             longest_string_list.remove(test_string[i])
#             i += 1
#     print(longest_number)
#
#
# longest_string("abcbzkloa")
#
# def longest_string(test_string):
#     i = 0
#     j = 0
#     longest_string_list = []
#     length_string = len(longest_string_list)
#     char_dict = {}
#
#     while i < len(test_string) and j < len(test_string):
#         if test_string[j] not in longest_string_list:
#             longest_string_list.append(test_string[j])
#             char_dict[test_string[j]] = j
#             if len(longest_string_list) > length_string:
#                 length_string = len(longest_string_list)
#             j += 1
#         else:
#             del longest_string_list[0:char_dict[test_string[j]] + 1]
#             i = char_dict[test_string[j]] + 1
#             char_dict[test_string[j]] = j
#
#     print(length_string)
#
#
# longest_string("abcdcbnmkl")
