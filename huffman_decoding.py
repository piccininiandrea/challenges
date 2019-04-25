"""
(from www.hackerrank.com)
Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies. 
More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords. All edges along the path to a character contain a code digit. 
If they are on the left side of the tree, they will be a 0 (zero). If on the right, they'll be a 1 (one). Only the leaves will contain a letter and its frequency count. 
All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its descendant characters.

For instance, consider the string ABRACADABRA. There are a total of 11 characters in the string. This number should match the count in the ultimately determined root of the tree.
Our frequencies are A = 5, B = 2, R = 2, C = 1 and D = 1.
The graph representing this Huffman coding looks like the following

  (None,11)
  0/     \1
(A,5)   (None,6)
        0/    \1
     (R,2)   (None,4)
             0/    \1
       (None,2)   (B,2)
       0/     \1
     (C,1)   (D,1)

This means that symbols A, R, B, C, D are decodes as following:
A - 0
B - 111
C - 1100
D - 1101
R - 10

Our Huffman encoded string for ABRACADABRA is:

A B    R  A C     A D     A B    R  A
0 111 10 0 1100 0 1101 0 111 10 0
or
01111001100011010111100 

Function Description
Complete the function decode_huff in the editor below. It must return the decoded string.
decode_huff has the following parameters:
root: a reference to the root node of the Huffman tree
s: a Huffman encoded string

Constraints
1 <= |s| <= 25

Output Format
Returns string with the decoded word.

Sample Input
s = 01111001100011010111100

Sample Output
ABRACADABRA

Explanation
see description above
"""

"""
class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""        


def decodeHuff(root, s):
    if root is None:
        return ''
    res = ''
    node = root
	#you can also use a while loop and manage the index yourself
	#in this way you can avoid the instruction res += node.data in the end
    for c in s: 
        if '0' == c and node.left is not None:
            node = node.left
        elif '1' == c and node.right is not None:
            node = node.right
        else:
            res += node.data
            node = root.left if '0' == c else root.right
    res += node.data
    return res