"""
(from www.hackerrank.com)
Monica wants to buy a keyboard and a USB drive from her favorite electronics store. The store has several models of each. Monica wants to spend as much as possible for the 2 items, given her budget.
Given the price lists for the store's keyboards and USB drives, and Monica's budget, find and print the amount of money Monica will spend. If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead. She will buy only the two required items.

Function Description
Complete the getMoneySpent function in the editor below. It should return the maximum total price for the two items within Monica's budget, or -1 if she cannot afford both items.
getMoneySpent has the following parameter(s):
keyboards: an array of integers representing keyboard prices
drives: an array of integers representing drive prices
b: the units of currency in Monica's budget

Constraints
1 <= n,m <= 1000
1 <= b <= 10^6
The price of each item is in the inclusive range [1, 10^6].

Output Format
Print a single integer denoting the amount of money Monica will spend. If she doesn't have enough money to buy one keyboard and one USB drive, print -1 instead.

Sample Input
b = 10
keyboards = [3, 1]
drives = [5, 2, 8]

Sample Output
9

Explanation 0

She can buy the 2nd keyboard and the 3rd USB drive for a total cost of 9.
"""

import os
import sys


def getMoneySpent(keyboards, drives, b):
    keyboards.sort() # with n = len(keyboards) -> O(n log(n))
    drives.sort() # with m = len(keyboards) -> O(m log(m))
    if keyboards[0] + drives[0] > b:
        return -1
    return helper(keyboards, drives, b, 0, 0, keyboards[0] + drives[0], dict())

def helper(keyboards, drives, b, k, d, cost, memo):
	if keyboards[k] + drives[d] > b:
		return cost
	elif keyboards[k] + drives[d] == b:
		return b
	else:
		c1 = c2 = keyboards[k] + drives[d]
		if k < len(keyboards) - 1:
			if memo.get((k+1,d)) is None:
				c1 = helper(keyboards, drives, b, k + 1, d, keyboards[k] + drives[d], memo)
				memo[(k+1,d)] = c1
			else:
				c1 = memo.get((k+1,d))
		if d < len(drives) - 1:
			if memo.get((k,d+1)) is None:
				c2 = helper(keyboards, drives, b, k, d + 1, keyboards[k] + drives[d], memo)
				memo[(k,d+1)] = c2
			else:
				c2 = memo.get((k,d+1)) 
		return max(c1, c2)
	# in the avarage case, this function cost O((n+m)/2) -> O(n+m)


if __name__ == '__main__':
	b = 10
	keyboards = [3, 1]
	drives = [5, 2, 8]
	print(getMoneySpent(keyboards, drives, b))
	
