import collections
from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False

    def insert(self, char):
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # n=num of words, l=letters in each word s = space taken by each letter of each word
        # time complexity:O(nl),
        # space complexity:O(nls)
        suffixes_list = []
        for k,v in self.children.items():
            if v.is_word:
                suffixes_list.append(suffix + k)
            if v.children:
                suffixes_list += v.suffixes(suffix + k)
        return suffixes_list


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # O(n) n is num of char in word
        current_node = self.root
        for ch in word:
            current_node = current_node.children[ch]
        current_node.is_word = True

    def find(self, prefix):
        # O(n) n is all keys under root
        current_node = self.root
        for ch in prefix:
            if ch in current_node.children:
                current_node = current_node.children[ch]
            else:
                return None
        return current_node

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
# test insert
for word in wordList:
    MyTrie.insert(word)
MyTrie.insert("test")
# test Find
print("Pass" if type(MyTrie.find("a")) is TrieNode else "Fail")
print("Pass" if MyTrie.find("b") is None else "Fail")
print("Pass" if type(MyTrie.find("t")) is TrieNode else "Fail")
# test suffixes
node = MyTrie.find("a")
print(node.suffixes())
print("Pass" if node.suffixes() == ["nt", "nthology", "ntagonist", "ntonym"] else "Fail")
node = MyTrie.find("t")
print(node.suffixes())
node = MyTrie.find("")
print(node.suffixes())

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')
interact(f,prefix='');

# Expected outputs
# Pass
# Pass
# Pass
# ['nt', 'nthology', 'ntagonist', 'ntonym']
# Pass
# ['rie', 'rigger', 'rigonometry', 'ripod', 'est']
# ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod', 'test']
#
# interactive(children=(Text(value='', description='prefix'), Output()), _dom_classes=('widget-interact',))

