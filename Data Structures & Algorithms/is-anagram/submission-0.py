class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = dict()
        for e in s:
            if e in map_s:
                map_s[e] += 1
            else:
                map_s[e] = 1
        for e in t:
            if e not in map_s:
                return False
            map_s[e] -= 1
            if map_s[e] == 0:
                del map_s[e]
        return map_s == {}
