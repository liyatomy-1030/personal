

for i in range(7):
    if i == 0:
        print("*" * 5)
    elif i < 5:
        print(" " * 4 + "*")
    elif i == 5:
        print(" *  *")
    else:
        print(" ***")

# Print the letter O using stars (*)
for i in range(7):
    if i == 0 or i == 6:
        print(" *** ")
    else:
        print("*   *")


# Print the letter H using stars (*)
for i in range(7):
    if i == 3:
        print("*" * 5)
    else:
        print("*" + " " * 3 + "*")


# Print the letter N using stars (*)
for i in range(7):
    print("*" + " " * i + "*" + " " * (6 - i) + "*")

