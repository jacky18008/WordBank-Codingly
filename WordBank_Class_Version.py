
# coding: utf-8

# In[1]:

import json
from pprint import pprint


# In[69]:

class WordBank():
    def __init__(self):
        self.wordbank = {}
        
    def search_dict(self, query):
    # A function to find the relative wordbank by a word.
    # However, for basic use, you only need to call the "add_dict" function below.
    
        for key in self.wordbank:
            if key == query:
                return self.wordbank[key]
            else:
                search_dict(self.wordbank[key], query) 

    def add_dict(self, new_keyword, target_keyword=""):
    # Add new keywords below another keyword that already exists.
    # For example: add_dict("Care about money", "Make more money", wordbank)
        if not target_keyword:
            self.wordbank[new_keyword] = {}
       
        else:
            target_dict = search_dict(self.wordbank, target_keyword)
            target_dict[new_keyword] = {}
    
        return self.wordbank
    
    def save_wordbank(self, wordbank_name = ""):
    # save your wordbank as a json file
    # the default file name is "WordBank", or you can use your own wordbank name.
    
        if not wordbank_name:
            wordbank_name = "WordBank"

        with open(wordbank_name + ".json", 'w') as fp:
            json.dump(self.wordbank, fp)
    
    def load_wordbank(self, wordbank_name = ""):
    # load your wordbank by a json file. 
    # the default file name is "WordBank", or you can use your own wordbank name.
    # Feel free to customize it! 
    
    # By the way2, the prefix "u'" means you word is in Unicode form, 
    # it won't appears when you really use the string.
        if not wordbank_name:
            wordbank_name = "WordBank"

        with open(wordbank_name + ".json", 'r') as fp:
            self.wordbank = json.load(fp)
            pprint(self.wordbank)

            return self.wordbank







