"""
(from www.hackerrank.com)
In this challenge, you must implement a simple text editor. Initially, your editor contains an empty string, S. You must perform Q operations of the following 4 types:
1: append(W) - append string W at the end of S
2: delete(K) - delete the last K chars of S
3: print(K) - print the Kth char of S
4: undo() - undo last operation of types 1 or 2

Input Fromat
First line from STD is Q, the number of operations.
Each line i of the Q subsequent lines (where 0 <= i <= Q) defines an operation to be performed. Each operation starts with a single integer, t (where t in {1,2,3,4}), denoting a type of operation as defined in the 
Problem Statement above. If the operation requires an argument,  is followed by its space-separated argument. For example, if t=1 and W=abcd, line i will be 1 abcd.

Constraints
1 <= Q <= 10^6
1 <= K <= |S|
The sum of the lengths of all W in the input <= 10^6
The sum of K over all delete operations <= 2*10^6
All input characters are lowercase English letters
It is guaranteed that the sequence of operations given as input is possible to perform 

Output Format
Each operation of type 3 must print the Kth character on a new line.

Sample Input
8
1 abc
3 3
2 3
1 xy
3 2
4 
4 
3 1

Sample Output
c
y
a

Explanation
S is initially empty S = ''
Q = 8
1: append 'abc to S -> S = 'abc'
2: print 3rd char of S -> print 'c'
3: delete last 3 chars of S -> S = ''
4: append 'xy' to S -> S = 'xy'
5: print the 2nd char of S -> print 'y'
6: undo the append at Q=4 -> S = ''
7: undo the delete at Q=3 -> S = 'abc'
8: print the 1st char of S -> print 'a'
"""

class Editor():
    def __init__(self):
        self.s = ''
		#store only the Delta of operations increase performance, otherwise with big input
		#you will consume memory and time
        self.prevs = [] #stack of the operations performed
        self.ops = {
            1: self.append,
            2: self.delete,
            3: self.printer,
            4: self.undo
        }
    
    def append(self,s):
        self.prevs.append((1,s)) #store only the Delta
        self.s = self.s + s

    def delete(self,k):
        self.prevs.append((2,self.s[(-int(k)):])) #store only the Delta
        self.s = self.s[:(-int(k))]

    def printer(self,k):
        print(self.s[int(k)-1])

    def undo(self):
        op,s = self.prevs.pop() #restore self.s based on the last operation performed
        if op == 1:
            self.s = self.s[:(-len(s))]
        if op == 2:
            self.s = self.s + s

Q = int(input())
text = Editor()
for i in range(Q):
    buff = input().split(' ')
    op = int(buff[0])
    f = text.ops.get(op)
    try:
        f(buff[1])
    except:
        f()