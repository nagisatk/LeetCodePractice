class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n1 = a.split('+')
        n2 = b.split('+')
        r1, v1, r2, v2 = int(n1[0]), int(n1[1][:-1]), int(n2[0]), int(n2[1][:-1])
        return str(r1*r2 - v1*v2) + '+' + str(r1*v2+r2*v1) + 'i'
if __name__ == '__main__':
    s = Solution()
    s.complexNumberMultiply("1+1i", "1+1i")
    s.complexNumberMultiply("1+-1i", "1+-1i")