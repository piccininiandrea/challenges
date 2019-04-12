"""
John is learning complexed math expressions. His book apparently contains print flaws and John wants to check if every expression has balanced brackets before start solving it.
Expressions contains brackets of the following type: (, [, {, ), ], }.

Function Description
Given a string of brackets, write a function which return true if the brackets are balanced, False otherwise.
The function has the following parameter(s):
s: a string of brackets

Constraints
1 <= |s| <= 10^3
s contains only bracket characters

Output Format
True or False

Sample Input
{[()()]}

Sample Output
True

Explanation
{ at index 0 is closed by } at index 7
[ at index 1 is closed by ] at index 6
( at index 2 is closed by ) at index 3
( at index 4 is closed by ) at index 5

NB: sequence like [({})] is perfectly fine even if ( includes {
"""

def balanceBrackets(s):
    stack = []
    braces = {'(':')','[':']','{':'}'}
    try:
        for b in s:
            if b == '(' or b == '[' or b == '{':
                stack.append(b)
            else:
                prev = stack.pop()
                if braces.get(prev,'') != b:
                    return False
    except:
        return Flase
    if len(stack) == 0:
        return True
    return False
	
print(balanceBrackets('{[()()]}')) #True
print(balanceBrackets('[({})]')) # True
print(balanceBrackets('[({])]')) # False
print(balanceBrackets('{[()]}{[()]()}{[(())]}')) # True
print(balanceBrackets('{[()]}{[()]()}{[(())]')) # False
