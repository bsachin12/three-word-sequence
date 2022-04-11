import  collections
import re
import sys
import os


try:
    os.remove('output.txt')
except OSError:
    pass

def open_file():     
   # Accept a file in command line
   # Syntax: py words.py file_name.txt        
   with open(sys.argv[1], 'r') as raw:
    read_text = raw.read().lower()
    return read_text        

def main(text): 
        index = 0 # for limiting print output
        # Split the text to count number of occurences
        words_in_a_file = [words for words in re.split("\W",read_text) if words]
        # Filter puctuations
        punc_list = '''!'\()-[]{};:"\,<>./?@#$%^&*_~'''    
        for punctuation in words_in_a_file:
         if punctuation in punc_list:
          words_in_a_file = words_in_a_file.replace(punctuation, "")
        # create triplets and feed them to collections.Counter (using tuple type so it's hashable)
        word_collection = collections.Counter(tuple(words_in_a_file[i:i+3]) for i in range(len(words_in_a_file)-3))
        for word_list in sorted([(k,v) for k,v in word_collection.items() if v>=1] ,key = lambda word_list : word_list[1],reverse=True):        
                index = index + 1
                # open file for write and limit output to 100 lines
                with open('output.txt', 'a') as out: 
                 print (word_list, file=out)
                 out.close()
                if index == 100:
                  break   
         
               

if __name__ == "__main__":
        read_text = open_file()
        main(read_text)
