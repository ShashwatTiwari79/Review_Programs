user_inp = input("Enter a string: ")

freq = {}


for char in user_inp:
    
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Find the first non-repeating character
for char in user_inp:
    if freq[char] == 1:
        print(f"The first non-repeating character is: {char}")
        break
else:
    print("No non-repeating character found.")
