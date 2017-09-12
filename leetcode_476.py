class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 1
        else:
            res = 0
            ep  = 1
            while num:
                if num % 2 == 0:
                    res += ep
                ep  <<= 1
                num >>= 1
            return res