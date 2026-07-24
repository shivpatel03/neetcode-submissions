class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [0] * n
        post = [0] * n
        result = [0] * n

        pre[0] = post[n-1] = 1

        # pre[i] should contain the prefix product
        # this means that for i=2, pre[2] should contain the product of everything to the left of it
        # post[2] should contain the product of everything to the right of it

        # create prefix array
        for i in range(1, n):
            # pre[1] = nums[0] * pre[0]
            pre[i] = nums[i - 1] * pre[i - 1]

        for i in range(n-2,-1,-1):
            post[i] = nums[i + 1] * post[i + 1]

        for i in range(n):
            result[i] = pre[i] * post[i]
        return result