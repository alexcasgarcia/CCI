# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.  Implement a method to count how many possible ways the child can run up the stairs.

def CountWaysUpStairs(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n == 2:
		return 1 + CountWaysUpStairs(n-2) + CountWaysUpStairs(n-1)
	elif n >= 3:
		return 1 + CountWaysUpStairs(n-3) + CountWaysUpStairs(n-2) + CountWaysUpStairs(n-1)

for x in xrange(40):
	print str(x) + " stairs has " + str(CountWaysUpStairs(x)) + " possibilities"
