#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Suffix-Tree Application
from suffix_trees import STree

class Node:
    def __init__(self, sub="", children=[]):
        self.sub = sub
        self.ch = children
class SuffixTree:
    def __init__(self, str):
        self.nodes = [Node()]
        for i in range(len(str)):
            self.addSuffix(str[i:])
 
    def addSuffix(self, suf):
        n = 0
        i = 0
        while i < len(suf):
            b = suf[i]
            x2 = 0
            while True:
                children = self.nodes[n].ch
                if x2 == len(children):
                    # no matching child, remainder of suf becomes new node
                    n2 = len(self.nodes)
                    self.nodes.append(Node(suf[i:], []))
                    self.nodes[n].ch.append(n2)
                    return
                n2 = children[x2]
                if self.nodes[n2].sub[0] == b:
                    break
                x2 = x2 + 1
 
            # find prefix of remaining suffix in common with child
            sub2 = self.nodes[n2].sub
            j = 0
            while j < len(sub2):
                if suf[i + j] != sub2[j]:
                    # split n2
                    n3 = n2
                    # new node for the part in common
                    n2 = len(self.nodes)
                    self.nodes.append(Node(sub2[:j], [n3]))
                    self.nodes[n3].sub = sub2[j:] # old node loses the part in common
                    self.nodes[n].ch[x2] = n2
                    break # continue down the tree
                j = j + 1
            i = i + j
            n = n2
 
    def visualize(self):
        if len(self.nodes) == 0:
            print ("<empty>")
            return
 
        def f(n, pre):
            children = self.nodes[n].ch
            if len(children) == 0:
                print ("└─", self.nodes[n].sub)
                return
            print ("├─", self.nodes[n].sub)
            for c in children[:-1]:
                print (pre, "|")
                f(c, pre + " | ")
            print (pre, "/")
            f(children[-1], pre + "  ")
 
        f(0, "")
    

def get_longest_palindromes(strng):
    N = len(strng)
    cache = [[None] * N for _ in range(N)]

    def is_palindrome(lo, hi):
        if cache[lo][hi] is not None:
            return cache[lo][hi]

        if lo == hi:
            return True
        elif lo + 1 == hi:
            return strng[lo] == strng[hi]

        ans = False if strng[lo] != strng[hi] else is_palindrome(lo+1, hi-1)
        cache[lo][hi] = ans
        return ans

    def generate_palindromes():
        ret = []
        longest = N
        found = False

        if not strng:
            return ['']

        for l in range(N, 0, -1):
            found = False
            for s in range(N-l+1):
                if is_palindrome(s, s+l-1):
                    found = True
                    ret.append(strng[s:s+l])
            if found:
                break
        return ret

    return generate_palindromes()

st = STree.STree("abc defghabcx xxabc")
a = ["xxxabcdxxx", "xxxadsaab", "ytyxxxsabrew", "qxxxqqabqw", "aaabxxx"]

#Driver Code:
print("\n")
print("....Pattern Searching....")
c=str(input("Enter String Value for pattern search:"))
print("located on this index: ",st.find(c))
print("\n")
print("...Longest repeated sub-String...")
b=str(input("enter string value for longest repeated substring:"))
print("Index Is: ",st.find_all(b))
print('\n')
print("Given List: ",a)
st = STree.STree(a)
print("...Longest Common Substring...")
print(st.lcs())
print("\n")
strng=("fooadmadambaristRacecar")
print("...Longest Palindrome In a String...")
print(get_longest_palindromes(strng))
print("\n")
print("****SUFFIX TREE REPRESENTATION****")
print("\n")
SuffixTree("Bear$").visualize()

