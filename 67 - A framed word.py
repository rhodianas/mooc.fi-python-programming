# Write your solution here
word = input("Word:")
i = int((28-len(word))/2)
j = i+1
print("*"*30)
if len(word) % 2 == 0:
    print("*"+" "*i+word+" "*i+"*")
else:
    print("*"+" "*i+word+" "*j+"*")
print("*"*30)
