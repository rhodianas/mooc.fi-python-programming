# Write your solution here
def all_the_longest(string_list):
    longest_strings = []
    longest = ""
    for item in string_list:
        if len(item) > len(longest):
            longest = item
    for item in string_list:
        if len(item) == len(longest):
            longest_strings.append(item)
    return longest_strings


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result)  # ['dorothy', 'richard']
