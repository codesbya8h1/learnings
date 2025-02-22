# Given two words, start and end, and a dictionary containing an array of words, return the length of the shortest transformation sequence to transform start to end. A transformation sequence is a series of words in which:

# Each word differs from the preceding word by exactly one letter.
# Each word in the sequence exists in the dictionary.
# If no such transformation sequence exists, return 0.

# Example:
# Input: start = 'red', end = 'hit',
#        dictionary = [
#             'red', 'bed', 'hat', 'rod', 'rad', 'rat', 'hit', 'bad', 'bat'
#        ]
# Output: 5
# Constraints:
# All words are the same length.
# All words contain only lowercase English letters.
# The dictionary contains no duplicate words.

def shortest_transformation_sequence(start, end, dictionary):
    # We will use a BFS to find the shortest transformation sequence
    # We will use a queue to store the words in the sequence
    # We will use a visited set to store the words we have visited
    # We will use a result list to store the words in the sequence
    queue = [(start, 1)]
    visited = set()
    while queue:
        word, length = queue.pop(0)
        if word == end:
            return length
        if word in visited:
            continue
        visited.add(word)
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in dictionary and new_word not in visited:
                    queue.append((new_word, length + 1))    
    return 0

start = 'red'
end = 'hit'
dictionary = ['red', 'bed', 'hat', 'rod', 'rad', 'rat', 'hit', 'bad', 'bat']

print(shortest_transformation_sequence(start, end, dictionary))