class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        if len(strs) is 0:
            return prefix

        min_length = len(min(strs, key=len))

        for i in range(min_length):
            character = strs[0][i]

            if all(s[i] == character for s in strs):
                prefix += character
            else:
                break

        return prefix
