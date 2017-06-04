# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()
    bad_position = 0
    unbalancedChars = False
    opening_brackets_stack = []
    for i, next in enumerate(text.strip()):
        bad_position+=1
        if next == '(' or next == '[' or next == '{':
            opening_brackets_stack.append(Bracket(next, i+1))
            pass
        if next == ')' or next == ']' or next == '}':
            if len(opening_brackets_stack) == 0:
                unbalancedChars = True
                break
            elif opening_brackets_stack[-1].Match(next) == False:
                unbalancedChars = True
                break
            else: opening_brackets_stack.pop()
    if unbalancedChars: print(bad_position)
    elif len(opening_brackets_stack) > 0: print(opening_brackets_stack[-1].position)
    else: print("Success")
