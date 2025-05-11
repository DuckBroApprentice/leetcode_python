class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowMap = {}
        for i in range(0,len(allowed)):
            allowMap[allowed[i]]=True
        count=0
        for i in range(0,len(words)):
            for j in range(0,len(words[i])):
                check = allowMap.get(words[i][j],False)
                if check != True:
                    break
                if j == len(words[i])-1:
                    count+=1
        return count
#runtime 252ms  Memory 14,81MB