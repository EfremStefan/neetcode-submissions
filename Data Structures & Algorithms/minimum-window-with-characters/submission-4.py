class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        res_dict = dict()
        t_dict = dict()
        for i in range(len(t)):
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        min_length = len(s) + 1
        l, start_index = 0, 0
        have = 0
        need = len(t_dict)
        for r in range(len(s)):
            if s[r] in t_dict:
                res_dict[s[r]] = res_dict.get(s[r], 0) + 1
                if res_dict[s[r]] == t_dict[s[r]]:
                    have += 1

            while have == need:
                if min_length > r - l + 1:
                    min_length = r - l + 1
                    start_index = l
                if s[l] in t_dict:
                    if res_dict[s[l]] == t_dict[s[l]]:
                        have -=1
                    res_dict[s[l]] -= 1
                l += 1
        if min_length > len(s):
            return ""
        return s[start_index:start_index + min_length]

            


            
            
            



        