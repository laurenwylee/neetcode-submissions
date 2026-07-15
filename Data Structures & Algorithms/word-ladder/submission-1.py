class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(wordList)):
                replace = word[:i] + "*" + word[i + 1:]
                graph[replace].append(word)     
        queue = deque([beginWord])
        visited = set([beginWord]) 
        count = 1
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    replace = word[:i] + "*" + word[i + 1:]
                    for x in graph[replace]:
                        if x not in visited:
                            visited.add(x)
                            queue.append(x)
                        
            count += 1
        return 0