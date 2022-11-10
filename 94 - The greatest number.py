# Write your solution here
def greatest_number(number1, number2, number3):
    if (number1 >= number2 and number1 >= number3):
        return number1
    if (number2 >= number1 and number2 >= number3):
        return number2
    if (number3 >= number1 and number3 >= number2):
        return number3


    # You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
