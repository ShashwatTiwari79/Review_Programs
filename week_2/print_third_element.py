def print_every_third(lst_nums):
    idx = 2  # Start from the third element (0-based index)
    while lst_nums:
        index = idx % len(lst_nums)  # Ensure index is within bounds
        print(lst_nums.pop(index))  # Remove and print the element
        idx += 2  # Move to the next third element

# Example usage:
lst = [10, 20, 30 , 40, 50, 60, 70, 80, 90]
print_every_third(lst)