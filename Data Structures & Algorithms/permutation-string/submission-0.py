class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_matrix = dict()
        for char in s1:
            freq_matrix[char] = freq_matrix.get(char, 0) + 1

        l = 0
        for r in range(len(s2)):
            if s2[r] in freq_matrix:
                freq_matrix[s2[r]] -= 1
            if all(value == 0 for value in freq_matrix.values()):
                return True
            if r - l + 1 == len(s1):
                if s2[l] in freq_matrix:
                    freq_matrix[s2[l]] = freq_matrix.get(s2[l], 0) + 1
                l+=1
            
        return False
                    


        
        