class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_dict = dict()
        max_length = 0
        l, r, = 0, 0
        while r < len(s):
            if s[r] in res_dict and res_dict[s[r]] >= l :
                l = res_dict[s[r]] + 1
            res_dict[s[r]] = r
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length
