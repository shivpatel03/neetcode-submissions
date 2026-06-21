class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create hashset, put numbers we have already seen in there
        hashSet = set()
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)

        return False