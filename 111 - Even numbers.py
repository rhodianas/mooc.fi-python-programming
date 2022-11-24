# Write your solution here
def even_numbers(a_list):
    even_numbers_list = []
    for item in a_list:
        if item % 2 == 0:
            even_numbers_list.append(item)
    return even_numbers_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)
