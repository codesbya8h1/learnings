from collections import deque

def word_ladder_length(beginWord, endWord, wordList):
    # Convert wordList to a set for O(1) lookups
    wordSet = set(wordList)
    
    # If endWord is not in wordSet, no transformation is possible
    if endWord not in wordSet:
        return 0

    # Initialize BFS queue with the starting word and step count
    queue = deque([(beginWord, 1)])  # (current_word, transformation_steps)

    while queue:
        print(queue)
        current_word, steps = queue.popleft()

        # If we reach the endWord, return the number of steps
        if current_word == endWord:
            return steps

        # Try all possible one-letter transformations
        for i in range(len(current_word)):
            original_char = current_word[i]
            for c in 'abcdefghijklmnopqrstuvwxyz':
                if c == original_char:
                    continue
                
                # Create a new word by replacing one character
                new_word = current_word[:i] + c + current_word[i+1:]
                # print(new_word)

                # If the new word is valid and in the word set
                if new_word in wordSet:
                    queue.append((new_word, steps + 1))
                    wordSet.remove(new_word)  # Mark as visited by removing it from the set

    # If no transformation sequence is possible
    return 0


wordList = ["hot", "dot","dog", "lot", "log", "cog"]
beginWord = "hit"
endWord = "cog"

print(word_ladder_length(beginWord, endWord, wordList))