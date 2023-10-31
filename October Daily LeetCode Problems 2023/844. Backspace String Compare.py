class Solution:
    def backspaceCompare(self, s, t):
        stack1 = []
        stack2 = []

        for c in s:

            if not stack1 and c == '#':
                continue
            elif c == '#':
                stack1.pop()
            else:
                stack1.append(c)

        for c in t:
            if not stack2 and c == '#':
                continue
            elif c == '#':
                stack2.pop()
            else:
                stack2.append(c)

        return ''.join(stack1) == ''.join(stack2)


