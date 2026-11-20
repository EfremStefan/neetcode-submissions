class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = dict()
        l, max_length, max_freq = 0, 0, 0
        for r in range(len(s)):
            res[s[r]] = res.get(s[r], 0) + 1

            max_freq = max(max_freq, res[s[r]])
            if r - l + 1 - max_freq <= k:
                max_length = max(r - l + 1, max_length)   
            else:
                if res[s[l]] == 1:
                    res.pop(s[l])
                else:
                    res[s[l]] -= 1
                l += 1

            
        return max_length
            
            
                




        