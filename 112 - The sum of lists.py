# Write your solution here
def list_sum(list1, list2):
    for i in range(0, len(list1)):
        list1[i] += list2[i]
    return list1


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))  # [8, 10, 12]
