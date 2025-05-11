class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        nums =[]
        res =0
        for i in range(0,n):
            nums.append(start + 2*i)
            res = res ^ nums[i]
        return res
#runtime 0ms Memory 12.45MB