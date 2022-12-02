# Write your solution here
def everything_reversed(list_of_strings):
    reversed_strings = []
    for item in list_of_strings:
        reversed_strings.append(f"{item[::-1]}")
    return reversed_strings[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)
