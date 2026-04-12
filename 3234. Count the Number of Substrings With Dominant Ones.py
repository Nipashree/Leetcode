# Problem:https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/?envType=daily-question&envId=2026-04-07

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zeros = [i for i, c in enumerate(s) if c == '0']
        total = 0

        # Case 1: substrings with no zeros (all ones)
        count = 0
        for c in s:
            if c == '1':
                count += 1
            else:
                total += count * (count + 1) // 2
                count = 0
        total += count * (count + 1) // 2

        m = len(zeros)

        # Case 2: substrings with z zeros
        for z in range(1, int(n**0.5) + 1):
            for i in range(m - z + 1):
                lz = zeros[i]
                rz = zeros[i + z - 1]

                left_limit = zeros[i - 1] if i > 0 else -1
                right_limit = zeros[i + z] if i + z < m else n

                # max extension
                left_choices = lz - left_limit
                right_choices = right_limit - rz

                base_len = rz - lz + 1
                base_ones = base_len - z

                need = z * z

                # try all left extensions
                for l in range(left_choices):
                    extra_left = l
                    remaining = need - (base_ones + extra_left)

                    if remaining <= 0:
                        total += right_choices
                    elif remaining < right_choices:
                        total += right_choices - remaining

        return total
