# Write your solution here
def list_of_stars(a_list):
    for item in a_list:
        stars = "*"*item
        print(stars)


if __name__ == "__main__":
    list_of_stars([3, 7, 1, 1, 2])
