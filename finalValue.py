class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        sum = 0
        for i in range(0,len(operations)):
            if operations[i][1] == '-':
                sum-=1
            if operations[i][1] == '+':
                sum+=1
        return sum
#runtime 3ms memory 12.38MB
    
class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        a = "++X"
        b = "X++"
        count =0
        for i in range(0,len(operations)):
            if operations[i] == a or operations[i] == b:
                count+=1
            else:
                count-=1
        return count
#runtime 0ms memory12.34MB