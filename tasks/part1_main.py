# Part 1 - Count Uniqe Words
import os

def unique_words(lst): 
    tset = set() # Creating an empty set
    for e in lst: # Adding strings in list to set
        tset.add(e)
    return len(tset) # Returns sum of strings in set

def most_used_words(lst):
    lst = [x for x in lst if len(x) >= 4] # Rebuilding the list with only words larger than 4
    dic = {} # Creating an empty dictionary
    for x in lst: # Adding strings in list to dictionary with values of how many times each of them exist in list
        if x not in dic: 
            dic[x] = 0
        dic[x] += 1 
    sor = sorted(dic.items(), key=lambda x: (-x[1], x[0])) # Sorting the dictionary, items with largest value first
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