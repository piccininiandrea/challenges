"""
(from hackerrank.com)
A queue is an abstract data type that maintains the order in which elements were added to it, 
allowing the oldest elements to be removed from the front and new elements to be added to the rear. 
This is called a First-In-First-Out (FIFO) data structure because the first element added to the queue 
(i.e., the one that has been waiting the longest) is always the first one to be removed.

A basic queue has the following operations:

Enqueue: add a new element to the end of the queue.
Dequeue: remove the element from the front of the queue and return it.
In this challenge, you must first implement a queue using two stacks. Then process q queries, 
where each query is one of the following 3 types:

- 1 x: Enqueue element  into the end of the queue.
- 2: Dequeue the element at the front of the queue.
- 3: Print the element at the front of the queue.

Input Format
The first line contains a single integer, q, denoting the number of queries. 
Each line i of the q subsequent lines contains a single query in the form described in the problem statement above. 
All three queries start with an integer denoting the query type, but only query 1 is followed by an additional 
space-separated value, x, denoting the value to be enqueued.

Constraints
- 1 <= q <= 10^5
- 1 <= type <= 3
- 1 <= |x| <= 10^9
- It is guaranteed that a valid answer always exists for each query of type 3.

Output Format
For each query of type 3, print the value of the element at the front of the queue on a new line.

Sample Input
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2

Sample Output
14
14
"""

class Queue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.ops = {
            1:self.enqueue,
            2:self.dequeue,
            3:self.printEl
        }

    def enqueue(self,value):
        if len(self.stack1) == 0:
            self._pouring(0)
        self.stack1.append(value)

    def dequeue(self):
        if len(self.stack1) != 0:
            self._pouring(1)
        return self.stack2.pop()

    def printEl(self):
        if len(self.stack1) != 0:#with real stack I couldn print stack1[0]
            self._pouring(1)
        print(self.stack2[-1])

    def getOp(self,op):
        return self.ops.get(op,None)
    
    def _pouring(self,mode):
        tmp1 = tmp2 = None
        if mode == 0:
            tmp1 = self.stack1
            tmp2 = self.stack2
        else:
            tmp1 = self.stack2
            tmp2 = self.stack1
        while len(tmp2) > 0:
            tmp1.append(tmp2.pop())


if __name__ == "__main__":
    queue = Queue()
    q = int(input())
    for i in range(q):
        user_input = input()
        op = list(map(int,user_input.split(" ")))
        f = queue.getOp(op[0])
        if f:
            try:
                f(op[1])
            except:
                f()