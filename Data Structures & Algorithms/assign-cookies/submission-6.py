class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        cookie, res = 0, 0

        s.sort()
        g.sort()

        if (len(s) == 0):
            return res
        for child in range(len(g)):
            while cookie < len(s) and g[child] > s[cookie]:
                cookie += 1
            
            if cookie < len(s) and g[child] <= s[cookie]:
                res += 1
                cookie += 1
                if (cookie == len(s)):
                    return res

        return res