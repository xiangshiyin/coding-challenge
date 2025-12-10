class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        The BFS solution
        """
        # exception:
        if not beginWord or not endWord or not wordList:
            return 0
        # Build the visited and word pattern lookup table
        visited = {}
        wordPattern = {}
        for word in wordList:
            # populate the visited lookup table
            if word not in visited:
                visited[word] = False
            # populate the pattern lookup table
            for pos in range(len(beginWord)):
                pattern = word[:pos] + "*" + word[pos + 1 :]
                if pattern not in wordPattern:
                    wordPattern[pattern] = [word]
                else:
                    wordPattern[pattern].append(word)
        print(visited)
        print(wordPattern)

        if endWord not in visited:
            return 0

        # BFS search
        from collections import deque

        queue = deque([[beginWord, 1]])

        while queue:
            # pull the head from the queue
            curr, level = queue.popleft()

            print(beginWord, endWord, curr, level)
            # process the head
            if level > 1 and curr == endWord:
                return level

            # push the children in
            for pos in range(len(beginWord)):
                pattern = curr[:pos] + "*" + curr[pos + 1 :]
                if pattern in wordPattern:
                    for w in wordPattern[pattern]:
                        if visited[w] == False:
                            queue.append([w, level + 1])
                            visited[w] = True
                    wordPattern[pattern] = []  # never use it again
            # print(queue)
        return 0
