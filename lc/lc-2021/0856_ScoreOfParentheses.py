class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        n = len(S)
        stack = []
        curr = 0

        for char in S:
            if char == "(":
                stack.append(curr)
                curr = 0
            else:
                curr = stack.pop() + max(2 * curr, 1)
            # print(stack)

        return curr
