# Write your solution here
def spruce(height):
    print("a spruce!")
    i = 1
    j = height
    while j > 0:
        space = " "*(j-1)
        print(space + "*"*i)
        i += 2
        j -= 1
    print(" "*(height-1)+"*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
