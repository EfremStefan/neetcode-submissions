class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = dict()
        l, max_length = 0, 0
        for r in range(len(s)):
            if s[r] not in res:
                res[s[r]] = 1
            else:
                res[s[r]] += 1

            most_common = 0
            for key in res:
                if res[key] > most_common:
                    most_common = res[key]
            if r - l + 1 - most_common <= k:
                max_length = max(r - l + 1, max_length)   
            else:
                if res[s[l]] == 1:
                    res.pop(s[l])
                else:
                    res[s[l]] -= 1
                l += 1

            
        return max_length
            
            
                




        