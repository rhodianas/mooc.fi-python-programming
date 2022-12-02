# Write your solution here
def most_common_character(my_string):
    maxcount = 0
    commonchar = ""
    for index in range(0, len(my_string)):
        count = my_string.count(my_string[index])
        if count > maxcount:
            maxcount = count
            commonchar = my_string[index]
    return commonchar


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    second_string = "exemplaryelementary"
    print(most_common_character(second_string))
