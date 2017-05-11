class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        num = x ^ y
        cnt = 0
        while num:
            num = num & (num-1)
            cnt ++
        return cnt