class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for j in t:
            
            if j in count:
                count[j] -= 1
            else:
                count[j] = -1

        for value in count.values():
            if value != 0 :
                return False
        return True