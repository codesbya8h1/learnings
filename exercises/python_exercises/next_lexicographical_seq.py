def next_lexicographical_sequence(s: str) -> str:
    # Convert string to a list for mutability
    chars = list(s)
    n = len(chars)
    
    # Step 1: Find the pivot
    i = n - 1
    while i > 0 and chars[i - 1] >= chars[i]:
        print("while 1: ",chars)
        i -= 1
    
    if i == 0:
        # The string is in descending order, return sorted order
        print("sorted : ",''.join(sorted(chars)))
        return ''.join(sorted(chars))
    
    # Step 2: Find the successor
    j = n - 1
    while chars[j] <= chars[i - 1]:
        print("While 2 : ",chars)
        j -= 1
    
    # Step 3: Swap pivot and successor
    chars[i - 1], chars[j] = chars[j], chars[i - 1]
    print("swapped : ",chars)
    
    # Step 4: Reverse suffix
    chars[i:] = reversed(chars[i:])
    print("reversed : ",chars)
    
    return ''.join(chars)

# Example usage
# print(next_lexicographical_sequence('abcd'))  # Output: 'abdc'
print(next_lexicographical_sequence('dcba'))  # Output: 'abcd'
