from dataclasses import dataclass
from typing import Any

@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        if key < self.key:  # If the key is smaller than the current node
            if self.left is not None:  # If left node exists, add under it
                self.left.put(key, value)  
            else:  # If left node doesn't exist, add left node
                self.left = Node(key, value, None, None) 
        elif key > self.key:  # If the key is bigger than current node:
            if self.right is not None:  # If right node exists, add under it
                self.right.put(key, value) 
            else:  # If right node doesn't exist, add right node
                self.right = Node(key, value, None, None) 
        else:  # If the key and current node are equal, current node has the key
            self.value = value

    def to_string(self):
        s = ""  # Create string
        if self.left is not None:  # If left node exist, add to "s" as string
            s += self.left.to_string()
        s += f"({self.key},{self.value}) "  # Add current node to "s" as string
        if self.right is not None:  # If right node exist, add to "s" as string:
            s += self.right.to_string()
        return s  # Return the string

    def count(self):
        size = 1  # Current node is 1
        if self.left is not None:  # If number under left node exist, add to integer "size"
            size += self.left.count()
        if self.right is not None:  # If number under right node exist, add to integer "size"
            size += self.right.count()
        return size  # Return integer "size"

    def get(self, key):
        value = None  # Default value is None
        if self.key == key:  # Return the value of current node if current node has the key
            return self.value  
        if self.left is not None:  # Find left node if exists
            if key <= self.key:  
                value = self.left.get(key)
                if value is not None:  # Return the value of left node when it's found
                    return value  
        if self.right is not None:  # Find right node if exists
            if key >= self.key:
                value = self.right.get(key)  
                if value is not None:  # Return the value of left node when it's found
                    return value  
        return value # Return None if left and right nodes doesn't exist

    def max_depth(self):
        md = 1  # Max depth is 1 from beginning
        ldepth = 0  # Integer value for left node from beginning
        rdepth = 0  # Integer value for right node from beginning
        if self.left is not None:  # If left node exists:
            ldepth += self.left.max_depth() # Increase left node value with depth of left node 
        if self.right is not None:  # If right node exists:
            rdepth += self.right.max_depth() # Increase right node value with depth of right node 
        if ldepth < rdepth:  # If depth of left node is bigger than right, increase max depth with left node depth
            md += rdepth
        else:  # If depth of right node is bigger than left, increase max depth with right node depth
            md += ldepth
        return md  # Return the max depth

    def count_leafs(self):
        left_counter = 0 # Left leafs
        right_counter = 0 # Right leafs
        if self.right is None and self.left is None: # If there are no leafs return 1
            return 1 
        else:
            if self.left is not None: # If there are left leafs, add it to integer "left_counter"
                left_counter = self.left.count_leafs()
            if self.right is not None: # If there are right leafs, add it to integer "right_counter"
                right_counter = self.right.count_leafs()
        return left_counter+right_counter # Return results


    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        lst = []  # An empty list
        tuple = (self.key, self.value)  # Get current node as tuple
        if self.left is not None:  # If left node exist, add it to list as tuple
            lst += (self.left.as_list(tuple))  
        lst.append(tuple)  # Add current node as tuple to list efter adding left node
        if self.right is not None:  # If right node exist, add it to list as tuple
            lst += (self.right.as_list(tuple))
        return lst  # Returns the list of tuples


@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes 
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
