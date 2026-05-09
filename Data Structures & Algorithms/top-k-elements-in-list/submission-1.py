class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # empty array of arrays
        freq = [[] for i in range(len(nums) + 1)]

        # getting the frequency map for each element
        count = Counter(nums)
        # looks like: nums[i]:frequency

        # for key, value in count
        # create frequency table, where index is the frequency
        # and values of an index is a list of the actual values (what they were in nums)
        for n, c in count.items():
            freq[c].append(n)

        result = []
        # need the top k elements
        # go from the end of the frequency hashmap
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result
