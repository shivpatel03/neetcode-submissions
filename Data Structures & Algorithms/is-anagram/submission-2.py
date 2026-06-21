class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # saves {letter:num occurences}
        mapS = Counter(s)

        for i in range(len(t)):
            if (t[i] in mapS):
                mapS[t[i]] = mapS[t[i]] - 1
            else:
                return False
        
        for value in mapS.values():
            if (value != 0):
                return False


        return True
            