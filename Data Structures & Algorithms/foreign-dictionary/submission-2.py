class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph = {c: set() for word in words for c in word}
        visited = defaultdict(int)
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            i = 0
            j = 0
            found_diff = False
            while i < len(w1) and j < len(w2):
                if w1[i] != w2[j]:
                    graph[w1[i]].add(w2[j])
                    found_diff = True
                    break
                i += 1
                j += 1
            if not found_diff and len(w1) > len(w2):
                return ""
        path = []
        def dfs(node):
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True
            visited[node] = 1
            for u in graph[node]:
                if dfs(u) == False:
                    return False
            visited[node] = 2
            path.append(node)
            return True

        for c in graph:
            if visited[c] == 0:
                if not dfs(c):
                    return ""

        path.reverse()
        return "".join(path)
