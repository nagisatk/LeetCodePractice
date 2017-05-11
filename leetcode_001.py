class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = 0
        while nums[index]:
            print (target - nums[index]) in nums[index+1:]
            if (target - nums[index]) in nums[index+1:]:
                return [index, nums[index+1:].index(target - nums[index]) + index + 1]
            index += 1
if __name__ == '__main__':
    s = Solution()
    nums = [0,4,3,0] 
    print nums[1:].index(0)
    a = s.twoSum(nums, 0)
    print a,