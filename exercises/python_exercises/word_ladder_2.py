from queue import deque
class Node:

    def __init__(self, word):
        self.word=word
        self.neighbors=[]
    
def build_graph(word_list):
    nodes = {word: Node(word) for word in word_list}

    # Connect nodes that differ by one character
    # for word in word_list:
    #     for i in range(len(word)):
    #         # Creates too many variables
    #         for c in 'abcdefghijklmnopqrstuvwxyz':
    #             new_word = word[:i] + c + word[i+1:]
    #             if new_word in nodes and new_word != word:
    #                 nodes[word].neighbors.append(nodes[new_word])


    # Connect nodes that differ by one character
    for i, word1 in enumerate(word_list):
        for word2 in word_list[i+1:]:
            if sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1:
                nodes[word1].neighbors.append(nodes[word2])
                nodes[word2].neighbors.append(nodes[word1])
    return nodes
    

def word_ladder_length(begin_word, end_word, word_list):
    # Add begin_word to the word_list if it's not already there
    if begin_word not in word_list:
        word_list.append(begin_word)
    
    # Build the graph
    graph = build_graph(word_list)
    
    # If end_word is not in the graph, no transformation is possible
    if end_word not in graph:
        return 0
    
    # BFS
    queue = deque([(graph[begin_word], 1)])
    visited = set([begin_word])
    
    while queue:
        current_node, level = queue.popleft()
        
        if current_node.word == end_word:
            return level
        
        for neighbor in current_node.neighbors:
            if neighbor.word not in visited:
                visited.add(neighbor.word)
                queue.append((neighbor, level + 1))
    
    # If no transformation sequence is possible
    return 0

# Example usage
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
begin_word = "hit"
end_word = "cog"

print(word_ladder_length(begin_word, end_word, word_list))
