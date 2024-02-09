function decode(input):
    create output string
    for each letter in input:
        get new_letter from letter's location in cipher
        add new_letter to output
    return output

# efficiency -> O(2n+2)
# for input -> "jzqh", n-> 4

# O(0n + 1) -> O(1)

def say_hello(n):
    for i in range(n):
        print("Hello!")

# efficiency -> O(n)

def say_hello(n):
    for i in range(n):
        for i in range(n):
            print("Hello!")

# efficiency -> O(n^2)
