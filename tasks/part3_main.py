# Part 3 - Count Uniqe Words 2
import HashSet as hset
import BstMap as bst
import os

unwords = hset.HashSet() # Create new empty HashSet
unwords.init() # Initialize with eight empty buckets
muwords = bst.BstMap() 

def unique_words(lst): 
    for word in lst: # Add words to HashSet, HashSet doesn't adds same words more than one
        unwords.add(word)
    output = f"{unwords.get_size()}" # Get size of elements in HashSet
    return output

def most_used_words(lst):
    lst = [x for x in lst if len(x) >= 4] # Rebuilding the list with only words larger than 4
    for i in lst: 
        wvalue = muwords.get(i) # Get values of words
        if wvalue is not None: # Calculating how many times each word exist
            wcount = wvalue + 1
            muwords.put(i, wcount) # Creating a Binary Search Tree with words and values
        else:
            muwords.put(i, 1) # If word exist only one time, adding to Bst with value 1
    sor = sorted(muwords.as_list(), key=lambda x: (-x[1], x[0])) # Sorting Bst dictionary, items with largest value first
    return sor # Returns sorted dictionary

path = os.getcwd()
n = 0
while n < 2: # A loop continues until all files are readed
    n+=1
    if n == 1:
        file = "/life_of_brian.txt" 
    else:
        file = "/swe_news.txt"
    lst = []
    with open(path+file, encoding="utf8") as f1: # Opens file 
        content = f1.read() # Reads the contents of the file 
        for i in content.split("\n"): # Adds all strings in content to list.
            lst.append(i)
    
    print("Number of unique words in", file ,"is:", unique_words(lst))
    
    dic = most_used_words(lst) 
    print("Top 10 most frequently used words in", file+":")
    for i in range(10): # Printing top 10 in the dictionary
        print(dic[i][0], dic[i][1])
    
    print() # To make printing look tidier on the terminal