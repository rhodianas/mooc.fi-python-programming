# Write your solution here
def no_shouting(list_of_strings):
    no_shouting_list = []
    for item in list_of_strings:
        if item.isupper():
            continue
        no_shouting_list.append(item)
    return no_shouting_list


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER",
               "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)
