from time import time

"""
    
    Doing a loop from [low, high] would suffice for this problem,
        as the upper bound of numbers to check is 10^6, resulting in O(N * K) where N is the size of range and K is the number of digits.
        
    That took ~250ms with Python2, and there are a lot of better ways to find the candidates:
        
        - Strictly nondecreasing digits will cut down most candidates (My input had only 476 numbers that fit this criteria!)
        
        This leads to a recursive function that generates all possible numbers digit-by-digit.
    
    What's more convenient is how we can easily find adjacent equal pairs.
    
    The following code takes < 1ms of time in Python2, which is way better than what I was aiming for :)
        

""

def solve(low, high):

    def helper(dig, num, cur, rep = 0, p1 = False, p2 = False):
    
        """
        dig => Number of digits
        num => Candidate number
        cur => Smallest digit we can place next
        rep => Number of consecutive digits that are identical
        p1  => Check if number satisfies part 1
        p2  => Check if number satisfies part 2
        """
    
        if dig == 6: # Grab 6-digit numbers
            if num < low or num > high: # Check bounds
                return False, False
            return p1, p2 or rep == 2 # Otherwise return the validity of the number for part 1 and 2
        
        # Case 1: Repeat the digit
        
        # This number will automatically become a valid candidate for part 1
        
        ans1, ans2 = helper(dig + 1, num * 10 + cur, cur, rep + 1, True, p2)
        
        for i in xrange(cur + 1, 10):
            
            # Case 2: Change the digit
            
            a, b = helper(dig + 1, num * 10 + i, i, 1, p1, p2 or rep == 2) # If rep == 2, then this number is a valid candidate for part 2
            ans1 += a
            ans2 += b
        
        return ans1, ans2

    return helper(0, 0, 0)

t0 = time()

p1, p2 = solve(372304, 847060)
print "Answer: %d for part 1, %d for part 2" % (p1, p2)
print "Time taken: %dms" % (1000 * (time() - t0))
