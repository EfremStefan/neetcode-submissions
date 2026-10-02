class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, el in enumerate(temperatures):
            while stack and stack[-1][0] < el:
                stack_el = stack.pop()
                result[stack_el[1]] = i - stack_el[1]
            stack.append((el, i))
        result[-1] = 0
        return result



        