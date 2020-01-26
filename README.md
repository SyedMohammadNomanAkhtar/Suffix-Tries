# Suffix-Tree
Suffix trees can be used to solve a large number of string problems that occur in text-editing, free-text search. 

# Working of Suffix-Tree
-The function visiualize takes a string strng and returns the visiualization of the tree and the time complexity of building a suffix tree is O(n^2).
SuffixTree("Bear$").visualize()
-Pattern searching function takes a string strng as input and search for the pattern in the given string and runs in O(m) times.
st = STree.STree("abcdefghab")
st.find("abc") 
-Searching string range function takes a string strng and returns the range of the given index.
(st.find_all("e"))
-Longest common substring function takes a string strng and return the longest common substring from the given string and runs in 0(n+m) times.

a = ["xxxabcxxx", "adsaabc", "ytysabcrew", "qqqabcqw", "aaabc"]
st = STree.STree(a)
print(st.lcs()) # "abc"
-Longest palindrome in a string function takes a string strng and reverse the index and returns the longest palindrome. It runs in O(nlogn) times.
strng=("fooadmadambaristracecar")
get_longest_palindromes(strng)
