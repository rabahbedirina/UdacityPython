num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0

len_num_list = len(num_list)

for i in range(len_num_list):
    if (num_list[i] % 2 != 0) and (count_odd < 5):
        list_sum += num_list[i]
        count_odd += 1
    # elif count_odd == 5:
    #     break
    print(num_list[i], count_odd)


print("The numbers of odd numbers added are: {}".format(count_odd))
print("The sum of the odd numbers added is: {}".format(list_sum))


num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542,
            87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list):
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    # elif count_odd == 5:
    #     break
    print(num_list[i], count_odd)
    i += 1

print("The numbers of odd numbers added are: {}".format(count_odd))
print("The sum of the odd numbers added is: {}".format(list_sum))
