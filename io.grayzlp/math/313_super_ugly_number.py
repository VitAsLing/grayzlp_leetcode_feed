"""
https://leetcode.com/problems/super-ugly-number/description/


Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k. For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

"""
import sys


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [0 for _ in xrange(n)]
        idx = [0 for _ in xrange(len(primes))]
        val = [1 for _ in xrange(len(primes))]

        next = 1
        for i in xrange(n):
            ugly[i] = next
            next = sys.maxint
            for j in xrange(len(primes)):
                if val[j] == ugly[i]:
                    val[j] = ugly[idx[j]] * primes[j]
                    idx[j] += 1
                next = min(next, val[j])
        return ugly[-1]


# Test code
print(Solution().nthSuperUglyNumber(6, [2, 3, 7]))
