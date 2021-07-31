def cti(ch):
    return ord(ch)-ord('a')
    
#Function to insert string into TRIE.    
def insert(root,key):
    
    #if not present, we insert key into trie. If the key is prefix 
    #of trie node, we just mark the leaf node.
    for e in key:
        idx=cti(e)
        
        if not root.children[idx]:
            root.children[idx]=TrieNode()
        
        root=root.children[idx]
    
    #marking last node as leaf.    
    root.isEndOfWord=True



#Function to use TRIE data structure and search the given string.
def search(root, key):
    
    for e in key:
        idx=cti(e)
        
        if not root.children[idx]:
            return
        
        root=root.children[idx]
    
    #returning true if key is present else false.
    return root.isEndOfWord