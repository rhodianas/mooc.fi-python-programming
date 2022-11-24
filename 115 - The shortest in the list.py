# Write your solution here
def shortest(string_list):
    shortest = string_list[0]
    for item in string_list:
        if len(item) < len(shortest):
            shortest = item
    return shortest


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)
