'''
Implementing a trie in Python just for fun

Made by Zack Smith 2-02-15
'''

# Node Class
class Node:
    # Each node is comprised of a key which is the letter of a word
    # And a child dictionary which contains every following node
    def __init__(self,data,parent):
        self.children = {}
        self.data = data

# Trie Class
class Trie:

    # Init Method
    def __init__(self):
        self.root = Node('*',None)
    
    # Add Node
    def add_word(self,word,curr_node): 
        ''' 
        Basic Logic: 
        Start at root
        Iterate over word, one letter at a time 
        If letter in children dict, continue to next child
        Else, create key and continue to next child
        Populate trie this way until all letters have been iterated through
        '''
        # If word is empty, we're done
        if (len(word) == 0):
            return
        # Set current node if undefined
        if (curr_node) == None: 
            curr_node = self.root
        # Grab data from first character of word
        data = word.pop(0)
        # Set up new node
        if data not in curr_node.children.keys():
            curr_node.children[data] = Node(data,curr_node)
        curr_node = curr_node.children[data]
        # Recall algorithm like a scrub
        self.add_word(word,curr_node)

    # Method to return suggestion after key press
    def return_suggestions(self,user_input):
        ''' 
        Traverse trie until end of user input or key does not exist
        return all children until null 
        '''
        curr_node = self.root
        try: 
            # Iterate over 'known' part of trie
            for letters in user_input: 
                print letters
                print curr_node.children.keys()
                curr_node = curr_node.children[letters]
        except: 
            print "No suggestions!"

            # Print everything in current node until they're done
            for child in curr_node.children.keys():
                # Print the user's input plus the rest of the trie
                temp_node = curr_node
                print user_input,
                while (len(temp_node.children) != 0):
                    print temp_node.data,
                    temp_node = temp_node
                    pass


def main():
    # Make a dictionary of a few sample words
    word_list = ['Apple','Orange','Banana','Fruit','Vegetable','Alpha','Apropos', 'Archangel','Angular','Amend','Alotted','Axial']
    # Create trie
    trie = Trie()
    # Add words in to trie
    for words in word_list:
        word = list(words)
        print 'Calling add word on ' 
        print word
        trie.add_word(word,None)
    # Suggest a word based on input
    trie.return_suggestions('Ap')

if __name__ == '__main__':
    main()
