class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        len0 =0
        for i in range(0,len(nums)):
            if nums[i]%2 == 0:
                len0+=1
        for i in range(0,len(nums)):
            if i >=len0:
                nums[i]=1
            else:
                nums[i]=0
        return nums
#runtime 0ms memory 12.58MB