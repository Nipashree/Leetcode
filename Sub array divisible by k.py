class Solution:
    def subarraysDivByK(self, nums, k):

        count = 0
        prefix = 0

        remainder = {0: 1}

        for num in nums:
            prefix += num

            rem = prefix % k

            if rem in remainder:
                count += remainder[rem]

            remainder[rem] = remainder.get(rem, 0) + 1

        return count
