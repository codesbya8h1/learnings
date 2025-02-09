def is_palindrome_valid(s: str) -> bool:    
    # Write your code here
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the filtered string is equal to its reverse
    return filtered == filtered[::-1]

print(is_palindrome_valid('a dog! a panic in a pagoda.'))