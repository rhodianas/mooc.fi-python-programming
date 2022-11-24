# Write your solution here
def sum_of_positives(a_list):
    sum = 0
    for item in a_list:
        if item > 0:
            sum += item
    return sum


if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print("The result is", result)
