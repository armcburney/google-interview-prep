class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        curr_count, longest_count = 0, 0
        char_indices = {}

        for i, c in enumerate(s):
            if c in char_indices:
                start_of_sequence_index = min(char_indices.values())
                curr_count -= char_indices[c] - start_of_sequence_index

                new_dict = {}
                for key, value in char_indices.items():
                    if value > char_indices[c]:
                        new_dict[key] = value
                char_indices = new_dict
            else:
                curr_count += 1

            if curr_count > longest_count:
                longest_count = curr_count
            char_indices[c] = i

        return longest_count
