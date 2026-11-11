class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        def validEdge(s1, s2):
            difference_count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    difference_count += 1
            return difference_count == 1

        neigh = defaultdict(list)
        for i in range(len(wordList)):
            cur_word = wordList[i]
            for j in range(i + 1, len(wordList)):
                next_word = wordList[j]
                if validEdge(cur_word, next_word):
                    neigh[cur_word].append(next_word)
                    neigh[next_word].append(cur_word)
        for i in range(len(wordList)):
            cur_word = wordList[i]
            if validEdge(cur_word, beginWord):
                neigh[cur_word].append(beginWord)
                neigh[beginWord].append(cur_word)
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        while queue:
            node, dist = queue.popleft()
            for nei in neigh[node]:
                if nei == endWord:
                    return dist + 1
                if nei not in visited:
                    visited.add(nei)
                    queue.append((nei, dist + 1))
        return 0
                

        