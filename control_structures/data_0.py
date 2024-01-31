def smallest_positive(in_list):
    smallest = float('inf')
    for item in in_list:
        if item > 0 and item < smallest:
            smallest = item
    return smallest

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2