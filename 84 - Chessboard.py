# Write your solution here
def chessboard(number):
    i = 0
    while i < number:
        j = 0
        while j < number:
            if (i == 0 and j == 0) or (i+j) % 2 == 0:
                print(1, end="")
            else:
                print(0, end="")
            j += 1
        print("")
        i += 1


# Testing the function
if __name__ == "__main__":
    chessboard(3)
