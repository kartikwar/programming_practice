'''
Trie data structure is a n-ary tree structure. 
Hence each node can have multiple children 
Trie data structures are used when there are a lot of 
sub strings common in words. 

                        *

            B                       S

      A        E                    A      

  T                 L               T    

$                       L           $
                            $


In the above trie implementation * denotes the root node.
$ denotes the end of word.

The words in this trie are bat, bell and sat
'''


class TrieNode:
  def __init__(self, letter):
    self.letter = letter
    self.children = {}
    self.is_end_of_word = False

class Trie:
  def __init__(self):
    self.root = TrieNode("*")
  
  def add_word(self, word):
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        curr_node.children[letter] = TrieNode(letter)
      curr_node = curr_node.children[letter]
    curr_node.is_end_of_word = True
  
  def does_word_exist(self, word):
    if word == "":
      return True
    curr_node = self.root
    for letter in word:
      if letter not in curr_node.children:
        return False
      curr_node = curr_node.children[letter]
    return curr_node.is_end_of_word 


if __name__ == '__main__':
    trie = Trie()
    words = ["wait", "waiter", "shop", "shopper"]
    for word in words:
        trie.add_word(word)

    print(trie.does_word_exist("wait")) #True
    print(trie.does_word_exist("")) #True
    print(trie.does_word_exist("waite")) #False
    print(trie.does_word_exist("shop")) #True
    print(trie.does_word_exist("shoppp")) #False