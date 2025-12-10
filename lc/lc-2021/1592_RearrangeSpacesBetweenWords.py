class Solution:
    def reorderSpaces(self, text: str) -> str:
        ws = text.strip().split()
        n = len(ws)
        num_spaces = len(text) - len(text.replace(" ", ""))
        if n > 1:
            space_per_slot = num_spaces // (n - 1)
            extras = num_spaces % (n - 1)
        else:
            space_per_slot = 0
            extras = num_spaces

        ans = (" " * space_per_slot).join(ws) + " " * extras
        return ans
