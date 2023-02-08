import BstMap as bst

dict = {"Ella": 39, "Owen": 40, "Fred": 44, "Zoe": 41, "Adam": 27, "Ceve": 37}
map = bst.BstMap()
for char, value in dict.items():
    map.put(char, value)
print(map.to_string())       
print("Size:", map.size())    

print("\nOverride existing values")
map.put("Zoe", 99)
map.put("Ceve", 100)
print(map.to_string())

print("\nGet Freds Value:", map.get("Fred")) 
print("Max depth:", map.max_depth())
print("Count leafs:", map.count_leafs())

map.put("AA", 1)
map.put("AAA", 2)
map.put("AAAA", 3)
map.put("AAAAA", 4)

print("\nSize:", map.size())
print("Max depth:", map.max_depth())
print("Count leafs:", map.count_leafs())
print("To string: ", map.to_string())

lst = map.as_list()
print("\nList size and element type:", len(lst), type(lst[0]))  
print("List content:", lst)
