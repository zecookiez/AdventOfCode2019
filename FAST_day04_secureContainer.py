from sys import setrecursionlimit
from time import time

setrecursionlimit(100000) # Don't let the stack overflow

def solve(low, high):

    low = map(int, str(low))
    high = map(int, str(high))

    memo = {}

    def helper(dig, cur, rep=0, p1=False, p2=False, gr=False, lo=False):

        """
        dig => Number of digits
        cur => Smallest digit we can place next
        rep => Number of consecutive digits that are identical
        p1  => Check if number satisfies part 1
        p2  => Check if number satisfies part 2
        gr  => Check if number is greater than lower
        lo  => Check if number is lower than high
        """

        if dig == len(low):  # Terminating condition
            return p1, p2 or rep == 2  # Return the validity of the number for part 1 and 2

        # We can reuse answers based on the parameters we currently have
        # Note that we can cap rep to 3, since anything beyond will get you the same results

        label = dig, cur, min(3, rep), p1, p2, gr, lo

        if label in memo: # memoization!
            return memo[label]

        ans1 = ans2 = 0

        # Change bounds depending on if the number currently fits in the range

        lower  = max(cur, 0 if gr else low[dig])
        higher = 9 if lo else high[dig]

        for i in xrange(lower, higher + 1):
            if i == cur:
                # Case 1: Repeat the digit
                # This number will automatically become a valid candidate for part 1
                a, b = helper(dig + 1,
                              i,
                              rep + 1,
                              True,
                              p2,
                              gr or i > low[dig],
                              lo or i < high[dig])
            else:
                # Case 2: Use a different digit from the previous
                # This may fit the condition for part 2 depending on the number of digits that were already repeated
                a, b = helper(dig + 1,
                              i,
                              1,
                              p1,
                              p2 or rep == 2,
                              gr or i > low[dig],
                              lo or i < high[dig])
            ans1 += a
            ans2 += b

        memo[label] = ans1, ans2
        return ans1, ans2

    return helper(0, low[0])

t0 = time()

p1, p2 = solve(pow(10, 1000), pow(10, 1001) - 1)
print("Answer: %d for part 1, %d for part 2" % (p1, p2))
print("Time taken: %.10f ms" % (1000 * (time() - t0)))
