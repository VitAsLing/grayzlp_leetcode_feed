"""
https://leetcode.com/problems/count-primes/description/

Description:

Count the number of prime numbers less than a non-negative number, n.

"""
import math


class Solution(object):
    def countPrimes(self, n):
        not_prime = [False] * n
        count = 0
        for i in range(2, n):
            if not not_prime[i]:
                count += 1
                j = 2
                while i * j < n:
                    not_prime[i * j] = True
                    j += 1
        return count

    # too slow
    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self.is_prime(i):
                count += 1
        return count

    def is_prime(self, k):
        for i in range(2, min(k, int(math.ceil(math.sqrt(k))) + 1)):
            if k % i == 0:
                return False
        return True


# Test code
print Solution().countPrimes(10)
