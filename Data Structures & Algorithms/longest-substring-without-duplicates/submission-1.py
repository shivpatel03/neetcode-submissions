class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        res = 0

        for right in range(len(s)):
            # while this number is in seen (has been seen before in the substring)
            while s[right] in seen:
                # remove the leftmost number until everything in seen is unique
                # and iterate by 1
                seen.remove(s[left])
                left += 1
            # if it's not seen, add it to the list
            seen.add(s[right])
            # return the maximum (right - left gives you current substring)
            res = max(res, right - left + 1)

        return res