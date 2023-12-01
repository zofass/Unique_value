def find_unique_value(some_list):
    count_list = []

    for num in some_list:
        found = False
        for item in count_list:
            if item[0] == num:
                item[1] += 1
                found = True
                break
        if not found:
            count_list.append([num, 1])

    for item in count_list:
        if item[1] == 1:
            return item[0]


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
