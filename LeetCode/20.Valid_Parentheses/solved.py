class Solution:

    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '[': ']', '{': '}'}
        if len(s) % 2 != 0:
            return False

        stack = []
        for item in s:
            if item in parentheses.keys():
                stack.append(item)
            else:
                if len(stack) <= 0:
                    return False
                else:
                    key = stack.pop()
                    if parentheses[key] != item:
                        return False
        if len(stack) > 0:
            return False
        return True
