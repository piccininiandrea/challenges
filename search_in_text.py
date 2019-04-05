"""
Sam is 12 years old and he wants to become a writer one day.
His teacher, Miss Mary suggested him to improve his lexicon, adding new words in his vocabulary and avoiding to use many times the same word.
For this purpose Sam wants you to write a function that having in input the text written by Sam and the dictionary given by Mary, 
searches in the text how many times each word of the dictiony appears in the text.

Function Description
The function returns an array of integers representing how many times each word of the dictionary appears in the text.
countingWords has the following parameters:
text - an array of strings which compose Sam's text
dictionary - an array of words to count in text

Input Format
2 arrays of string, text of length n and dictionary of length m

Constraints
1 <= n, m <= 1000
1 <= |text[i]|, |dictionary[i]| <= 30
text[i], dictionary[i] are lower case

Output Format
1 array of length m

Sample Input
text = ['the', 'street', 'is', 'small', 'and', 'my', 'cat', 'is', 'small']
dictionary = ['narrow', 'small', 'tiny']

Sample Output
[0, 2, 0]
"""

def matchingStrings(text, dictionary):
    res = [0] * len(dictionary)
    sdict = {}
    for a in text:
        sdict[a] = sdict.get(a,0) + 1
    for i,q in enumerate(dictionary):
        res[i] = sdict.get(q,0)
    return res


if __name__ == '__main__':
	text = ['the', 'street', 'is', 'small', 'and', 'my', 'cat', 'is', 'small']
	dictionary = ['narrow', 'small', 'tiny']
	print(matchingStrings(text, dictionary)) # [0,2,0]
	text = ['law', 'and', 'lawyer', 'behind', 'me', 'and', 'behind', 'you', 'like', 'you', 'behind', 'it']
	dictionary = ['law', 'lawyer', 'behind', 'and', 'you', 'that']
	print(matchingStrings(text, dictionary)) # [1,1,3,2,2,0]