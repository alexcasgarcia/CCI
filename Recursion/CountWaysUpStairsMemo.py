# A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.  Implement a method to count how many possible ways the child can run up the stairs.

def CountWaysUpStairs(n):
	return _CountWaysUpStairs(n,{})

def _CountWaysUpStairs(n,memo):
	if n == 0 or n == 1:
		return 1
	if not memo.has_key(n):
		if n == 2:
			memo[2] = 1 + _CountWaysUpStairs(n-2,memo) + _CountWaysUpStairs(n-1,memo)
		elif n >= 3:
			memo[n] = 1 + _CountWaysUpStairs(n-3,memo) + _CountWaysUpStairs(n-2,memo) + _CountWaysUpStairs(n-1,memo)
	return memo[n]
for x in xrange(40):
	print str(x) + " stairs has " + str(CountWaysUpStairs(x)) + " possibilities"
