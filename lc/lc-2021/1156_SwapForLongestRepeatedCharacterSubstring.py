class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        # special cases
        if n == 1:
            return 1

        # find continuous blocks
        ref = 0
        start = 0
        end = start
        ix = 1
        blocks = []
        while ix < n:
            if text[ix] == text[start]:
                end += 1
            else:
                blocks.append((start, end))
                start = ix
                end = ix
            ix += 1
        blocks.append((start, end))
        print(blocks)

        # build hash table to record character frequency
        from collections import Counter

        freq = Counter(text)

        # traverse the blocks, get the length
        ans = 0
        for i in range(len(blocks)):
            start, end = blocks[i]
            if i + 1 < len(blocks):
                if i + 2 >= len(blocks):
                    # print(start, end, 'c1')
                    if freq[text[start]] > end - start + 1:
                        ans = max(ans, end - start + 2)
                    else:
                        ans = max(ans, end - start + 1)
                elif (
                    text[blocks[i + 2][0]] == text[start]
                    and blocks[i + 2][0] == end + 2
                ):  # can connect the next block
                    # print(start, end, 'c2')
                    if (
                        freq[text[start]]
                        > end - start + blocks[i + 2][1] - blocks[i + 2][0] + 2
                    ):
                        ans = max(
                            ans, end - start + blocks[i + 2][1] - blocks[i + 2][0] + 3
                        )
                    elif (
                        freq[text[start]]
                        == end - start + blocks[i + 2][1] - blocks[i + 2][0] + 2
                    ):
                        ans = max(
                            ans, end - start + blocks[i + 2][1] - blocks[i + 2][0] + 2
                        )
                    else:
                        ans = max(ans, end - start + 1)
                else:
                    # print(start, end, 'c3')
                    if freq[text[start]] > end - start + 1:
                        ans = max(ans, end - start + 2)
                    else:
                        ans = max(ans, end - start + 1)
            else:
                # print(start, end, 'c4')
                if freq[text[start]] > end - start + 1:
                    ans = max(ans, end - start + 2)
                else:
                    ans = max(ans, end - start + 1)
        return ans
