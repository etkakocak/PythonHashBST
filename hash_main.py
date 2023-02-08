import HashSet as hset

words = hset.HashSet()   # Create new empty HashSet
words.init()             # Initialize with eight empty buckets

# Add names to word set.
# More than eight names ==> will trigger rehash
names = ["Ella", "Owen", "Fred", "Zoe", "Adam", "Ceve", "Adam", "Ceve", "Jonas", "Ola", "Morgan", "Fredrik", "Simon", "Albin", "Jonas", "Amer", "David"]
for name in names:
    words.add(name)

print("\nTo string:", words.to_string())
print("Size:", words.get_size())
print("Contains Fred?:", words.contains("Fred"))
print("Contains Bob?:", words.contains("Bob"))

# Hash specific data
mx = words.max_bucket_size()
print("\nMax bucket:", mx)
buckets = words.bucket_list_size()
print("Bucket list size:", buckets)
zero_buckets_ratio = words.zero_bucket_ratio()
print("Zero bucket ratio:", round(zero_buckets_ratio, 2))

# Remove elements
delete = ["Ceve", "Adam", "Ceve", "Jonas", "Ola"]
for s in delete:
    words.remove(s)
print("\nSize:", words.get_size())
print("To string:", words.to_string())
