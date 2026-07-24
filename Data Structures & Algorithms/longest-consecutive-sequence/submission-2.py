class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in nums:
            # is this the START of a sequence
            # we check if -1 is not in the array because anything -1 would NOT be the START of a sequence
            # this checks if this number DOESN'T have a left neighbour
            if (num - 1 not in numset):
                length = 0
                while(num + length) in numset:
                    length += 1
                longest = max(longest, length)

        
        return longest