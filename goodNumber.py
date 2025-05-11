class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i<j:
                    count+=1
    
        return count
    
class Solution(object):
    def numIdenticalPairs(self, nums):

        dist_elements = set(nums)
        my_map = {}

        for i, v in enumerate(dist_elements):
            my_map[v] = 0

        for i in nums:
            my_map[i] += 1  

        combs = 0
        for i in my_map.values():
            if i > 1:
                combs += i * (i - 1) // 2
            else:
                pass

        return combs

nums = [1,2,3,1,1,3]

solution = Solution()
solution.numIdenticalPairs(nums)