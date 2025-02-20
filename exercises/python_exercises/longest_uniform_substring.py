# Longest Uniform Substring After Replacements
# Hard
# A uniform substring is one in which all characters are identical. Given a string, determine the length of the longest uniform substring that can be formed by replacing up to k characters.

# Example:


# Input: s = 'aabcdcca', k = 2
# Output: 5
# Explanation: if we can only replace 2 characters, the longest uniform substring we can achieve is "ccccc", obtained by replacing 'b' and 'd' with 'c'.

from collections import defaultdict

def longestUniformSubstring(s: str, k: int) -> int:
    char_count = defaultdict(int)
    max_freq = 0
    max_length = 0
    left = 0
    
    for right in range(len(s)):
        char_count[s[right]] += 1
        max_freq = max(max_freq, char_count[s[right]])
        
        if (right - left + 1) - max_freq > k:
            char_count[s[left]] -= 1
            left += 1
        
        max_length = max(max_length, right - left + 1)
        print(f"current left:{left}, current right:{right}, left char: {s[left]}, right char: {s[right]}, max_length: {max_length}, char_count: {char_count}")
        
    
    return max_length

# Example usage
s = "aabcdcca"
k = 2
result = longestUniformSubstring(s, k)
print(f"Length of longest uniform substring: {result}")
