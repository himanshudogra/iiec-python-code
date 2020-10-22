a_list = [1, 3, 2, 3,4,5,3,5,2,6,7,8,5,4,10,10]

max_value = max(a_list)

print(max_value)

indices = [index for index, value in enumerate(a_list) if value == max_value]

print(indices)