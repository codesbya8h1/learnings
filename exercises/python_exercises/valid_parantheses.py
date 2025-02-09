# Given a string representing an expression of parentheses containing the characters '(', ')', '[', ']', '{', or '}', determine if the expression forms a valid sequence of parentheses.

# A sequence of parentheses is valid if every opening parenthesis has a corresponding closing parenthesis, and no closing parenthesis appears before its matching opening parenthesis.

# Example 1:
# Input: s = '([]{})'
# Output: True
# Example 2:
# Input: s = '([]{)}'
# Output: False
# Explanation: The '(' parenthesis is closed before its nested '{' parenthesis is closed.
def valid_parenthesis_expression(s: str) -> bool:
    # Write your code here
    stack = []
    mapping = {')':'(','}':'{', ']':'['}

    for char in s:
        if char in mapping:
            top_element  = stack.pop()

            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack

s = '([]{})'
print(valid_parenthesis_expression(s))
s = '([]{)}'
print(valid_parenthesis_expression(s))