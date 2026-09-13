class TreeNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TreeNode()
            cur = cur.children[c]

        cur.is_word = True

    def search(self, word: str) -> bool:
        # if it's a '.', insert all chidlren in queue with current index in searched word (node, search_idx)
        # when word found return True, return False when queue empty 
        if not word:
            return True
        queue = deque([(self.root, 0)])
        while queue:
            node, word_idx = queue.popleft()
            if word_idx == len(word): # for '.' as last char 
                if node.is_word:
                    return True
                continue
            cur_char = word[word_idx]
            if (
                word_idx == len(word) - 1 and cur_char in node.children and 
                node.children[cur_char].is_word
            ):
                return True
            if cur_char == '.':
                for child in node.children:
                    queue.append((node.children[child], word_idx + 1))
            else:
                if cur_char in node.children:
                    queue.append((node.children[cur_char], word_idx + 1))

        return False


class WordDictionary:

    def __init__(self):
        self.prefix_tree = PrefixTree()

    def addWord(self, word: str) -> None:
        self.prefix_tree.insert(word)

    def search(self, word: str) -> bool:
        return self.prefix_tree.search(word)
