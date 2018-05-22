class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        longest_sequence = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                curr_sequence = 0
                curr_num = num

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_sequence += 1

                longest_sequence = max(longest_sequence, curr_sequence)

        return longest_sequence
