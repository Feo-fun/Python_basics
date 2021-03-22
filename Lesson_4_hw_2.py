num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

bigger_num = [num_list[num] for num in range(1, len(num_list)) if num_list[num] > num_list [num - 1]]

print(bigger_num)