# Write your solution here
def distinct_numbers(a_list):
    a_list = sorted(a_list)
    distinct_list = []
    for item in a_list:
        if item not in distinct_list:
            distinct_list.append(item)
    return distinct_list


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))  # [1, 2, 3]
