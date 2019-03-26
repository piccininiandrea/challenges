"""
Given 2 strings s1 and s2, print the longest substring they have in common. The substring is not forced to be composed by consecutive letters, 
but given l1 = substring[k] and l2 = substring[k+1] then 
s1[i] = l1 and s1[j] = l2 with i<j
s2[x] = l1 and s1[y] = l2 with x<y

Function Description
Writing a function (longest_sub) which takes 2 string as parameters and prints the longest common substring
longest_sub has the following parameter(s):
s1: a string
s2: a string

Input Format
The first line contains a single integer denoting the length of s. 
The second line contains string s.

Constraints
0 <= |s1| <= 10^9
0 <= |s2| <= 10^9

Output Format
Print a string with the longest substring.

Sample Input
ABAZDC
BACBAD

Sample Output
ABAD

Explanation
s1:  ABA_D_
s2:  _A_BAD
"""

result = []
def longest_sub(s1,s2): # I use this function to clear result, check the edge cases and set lopngest() params
	result.clear()
	if s1 == '' or s2 == '':
		print('')
		return
	for i,e in enumerate(s1):
		longest(s1,s2,i,0,'',0)
	print(max(result,key=len))
	
		
def longest(s1,s2,i1,i2,r,l2):
	if i1 == len(s1):
		result.append(r)
		return
	if i2 >= len(s2):
		i1 += 1
		i2 = l2
		longest(s1,s2,i1,i2,r,i2)
	else:
		if s1[i1] == s2[i2]:
			longest(s1,s2,i1+1,i2+1,r+s1[i1],i2 + 1)
		else:
			longest(s1,s2,i1,i2+1,r,l2)
			

longest_sub('ABAZDC', 'BACBAD') #ABAD
longest_sub('AGGTAB', 'GXTXAYB') #GTAB
longest_sub('abba', 'abcaba') #abba
longest_sub('ebano', 'banoe') #bano
longest_sub('', 'abcaba') #''
longest_sub('qBweurfrfeoqwenpi', 'zxBucmfzxfvoxn') #Buffon
longest_sub('aaaa', 'aa') #aa
