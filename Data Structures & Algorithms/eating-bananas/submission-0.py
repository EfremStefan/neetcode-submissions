class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, 1
        for el in piles:
            if r < el:
                r = el
        res_k = r
        while (l <= r):
            k = l + (r - l) // 2
            h_needed = 0
            for pile in piles:
                h_needed += math.ceil(float(pile) / k)
            if h_needed > h:
                l = k + 1
            elif h_needed <= h:
                res_k = k
                r = k - 1
        return res_k

            
            

        