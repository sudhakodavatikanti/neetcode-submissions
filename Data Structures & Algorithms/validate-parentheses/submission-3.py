class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }

        if s[0] in my_dict.values() or len(s) < 2:
            return False

        my_stack = []
        for char in s:
            if char in my_dict.keys():
                my_stack.append(char)
            elif char in my_dict.values() and (len(my_stack) != 0 and my_dict[my_stack[-1]] == char):
                my_stack.pop()
            else:
                return False

        if len(my_stack) == 0:
            return True
        else:
            return False
        