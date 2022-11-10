# Write your solution here
def same_chars(text, index1, index2):
    if index1 < len(text) and index2 < len(text):
        if text[index1] == text[index2]:
            return True
    return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))
