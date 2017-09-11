class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lr = 0
        ud = 0
        for ch in moves:
            if ch == 'U':
                ud += 1
            elif ch == 'D':
                ud -= 1
            elif ch == 'R':
                lr += 1
            else:
                lr -= 1
        if lr or ud:
            return False
        else:
            return True