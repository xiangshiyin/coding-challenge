class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        operators = set(["+", "-", "*", "/"])
        stack = []
        i = 0

        while i < n:
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                if len(stack) >= 2:
                    r = stack.pop()
                    l = stack.pop()
                    # print(i, l, r)
                    if tokens[i] == "+":
                        tmp = l + r
                    elif tokens[i] == "-":
                        tmp = l - r
                    elif tokens[i] == "*":
                        tmp = l * r
                    elif tokens[i] == "/":
                        tmp = abs(l) // abs(r) if l * r > 0 else -1 * (abs(l) // abs(r))
                    stack.append(tmp)
                else:
                    return None
            # print(i, stack)
            i += 1
        if len(stack) == 1:
            return stack[0]
        else:
            return None
