from collections import Counter

# Input: s = 'caabab', t = 'aba'
# Output: 2
def substring_anagrams(s: str, t: str) -> int:
    # Write your code here.
    if len(t) > len(s):
        return 0
    
    t_count = Counter(t)
    window_count = Counter(s[:len(t)])
    result = 0
    if t_count == window_count:
        result += 1

    print("t_count :", t_count)
    print("window_count :", window_count)
    for i in range(len(t), len(s)):
        # Add new character to the window
        window_count[s[i]] += 1

        # Remove the character that goes out of the window
        start_char = s[i - len(t)]
        if window_count[start_char] == 1:
            del window_count[start_char]
        else:
            window_count[start_char] -= 1

        print("t_count :", t_count)
        print("window_count :", window_count)
        # Compare current window with t_count
        if window_count == t_count:
            result += 1

    return result
    

print(substring_anagrams(s = 'caabab', t = 'aba'))