#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
from BitVector import BitVector
import numpy as np
    
def Bloomfilter(key, m):
   
    # Create a bit Array of size m
    bits = BitVector(size=m)
    print(bits)
    
    # Set the key Word to a list
    key_list = list(key)
    print(key_list)
    
    # Create Hash Lists
    
    ASCII_VALUE_LIST = []
    
    HASH1 = []
    
    HASH1_append = []
    
    HASH2 = []
    
    HASH2_append = []
    
    HASH3 = []
    
    HASH3_append = []
    
    HASH4 = []
    
    # Return the ASCII Codes of the letters in the world list
    
    for i in range(len(key_list)):
        ASCII_VALUE= ord(key_list[i])
        
        ASCII_VALUE_LIST.insert(i, ASCII_VALUE)
        
    print( ASCII_VALUE_LIST)
    
    # Hashing Operations
    
    # 1. Hashing of values in the list
    
    for j in range(len(ASCII_VALUE_LIST)):
        # First Hashing of the values
        hash1 = ASCII_VALUE_LIST[j] % m
        
        HASH1.insert(j,hash1)
    print(HASH1)
    
    # 2. Appending a value to each member of the list(uniform distribution) since we are using a single hash function. 
    for x in HASH1:
         HASH_1 = x+1
         HASH1_append.insert(x,HASH_1)
            
    print( HASH1_append)
            
     # 1. Hashing of values in the list as second hash
    
    for k in range(len(HASH1_append)):
        # second Hashing of the values
        hash2 = HASH1_append[k] % m
        
        HASH2.insert(k,hash2)
    # 2. Appending a value to each member of the list(uniform distribution) since we are using a single hash function. 
    for x in HASH2:
         HASH_2 = x+2
         HASH2_append.insert(x,HASH_2)
            
    print( HASH2_append)
    
      # 1. Hashing of values in the list as second hash 
    
    for l in range(len(HASH2_append)):
        # third Hashing of the values
        hash3 = HASH2_append[l] % m
        
        HASH3.insert(l,hash3)
 
      # 2. Appending a value to each member of the list(uniform distribution) since we are using a single hash function. 
    for x in HASH3:
         HASH_3 = x+3
         HASH3_append.insert(x,HASH_3)
        
    print(HASH3_append)
        
     # 1. Hashing of values in the list(Last Hash function)
    for n in range(len(HASH3_append)):
        # fourth Hashing of the values
        hash4 = HASH3_append[n] % m
        
        HASH4.insert(l,hash4)
   
    
    
    # Setting the bloom filter up by turning a zero to one at the index represented on the bloom filter by the hash value
    
    for p in range(len(HASH4)):
        bits[HASH4[p]]=1
    print(bits)


# In[ ]:




