from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        z = 1
        n = 0 # A value of 0 that to be used for add
        for x in word: # For each character in word
            n+=ord(x)**z # Add unicode to n value
            z+=1 # To make hash value more unique
        hv = n % len(self.buckets) # Get a hash value
        return hv

    # Doubles size of bucket list
    def rehash(self):
        bucket = []  # An empty list to add the elements of the set
        for x in self.buckets: # Adding elements of the set to list
            for e in x:
                bucket.append(e)
        for i in range(len(self.buckets)): # Clearing the set
            self.buckets[i] = []  # Empty bucket
        self.size = 0  # Empty bucket size 0
        for i in range(len(self.buckets)): # Double the bucket
            self.buckets.append([]) 
        for element in bucket: # Add elements of set into new buckets
            self.add(element)

    # Adds a word to set if not already added
    def add(self, word):
        hash_value = self.get_hash(word) # Return hash for word
        if word in self.buckets[hash_value]: 
            return
        self.buckets[hash_value].append(word)  # Add hash word to bucket
        self.size += 1  # Increase set size with 1
        if self.size == len(self.buckets):   # If set size = buckets, rehash
            self.rehash()

    # Returns a string representation of the set content
    def to_string(self):
        s = "{ " # Create string
        for i in range(0, len(self.buckets)): # Add all elements in set to string "s"
            for x in self.buckets[i]:
                s += f"{x} "
        s += "}" # String created
        return s # Return the string

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        hash_value = self.get_hash(word)  # Return hash for word
        if word in self.buckets[hash_value]:  # Checks if specific word in the hash bucket
            return True  # Set contains the word
        else:
            return False  # Set doesn't contain the word

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        try:  # Using "try" so remove works without contains method
            hash_value = self.get_hash(word)  # Return hash for word
            self.buckets[hash_value].remove(word)  # Remove word from bucket list
            self.size -= 1  # Reduce set size by 1
        finally:  # Using "finally" so returns after removing element or does nothing
            return

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        k = 0  # A value of 0 that will change to value of biggest size
        for i in self.buckets:  # Each bucket in set
            if len(i) > k:  # If size of elements in bucket bigger than k value
                k = len(i)  # It's the biggest now, loop will continue until finding size of the bucket with most elements
        return k

    # Returns the ratio of buckets of lenght zero.
    # That is: number of zero buckets divided by number of buckets
    def zero_bucket_ratio(self):
        zero_bucket = 0 # Buckets with lenght zero
        other = 0 # All buckets
        for i in self.buckets: # Elements in bucket
            other += 1 # Add 1 to integer "other" (All buckets) for each bucket
            if len(i) == 0: # Add 1 to integer "zero_bucket" for each bucket with lenght zero
                zero_bucket += 1
        return zero_bucket / other # Return zero bucket ratio
