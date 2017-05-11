#! python
import random
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum
        
if __name__ == '__main__':
    s = Solution()
    nums = []
    for i in range(0, 5000):
        nums.append(random.randint(-10000, 10000))
    print s.arrayPairSum(nums)
    # print nums
