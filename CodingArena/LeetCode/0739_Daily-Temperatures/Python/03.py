"""
Author: Mrunal Nirajkumar Shah
Date  : 17th February, 2026

LeetCode: 739. Daily Temperature

Solution Description:
Time Complexity: O(n^2) ~ better than first two solutions (01.py and 02.py)
Space Complexity: O(2 * n) = O(n) ; n is number of temperature values

Remember:
Why this works?
My assumption was wrong. If 

X Y Z
if Z < Y; then no need to check for Z > X. This cuts the overall time complexity.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] *  len(temperatures)

        for i, temperature in enumerate(temperatures):
            if stack == []:
                stack.append(i)
                continue

            while stack and temperature > temperatures[stack[-1]]:
                answer[stack[-1]] = i - stack[-1]

                stack.pop()

            stack.append(i)
            
        return answer
            


def main():
    list_temperatures = [[73,74,75,71,69,72,76,73],
                         [30,40,50,60],
                         [30,60,90]
                         ]
    
    solve = Solution()

    result = []
    for temperatures in list_temperatures:
        result.append(solve.dailyTemperatures(temperatures))

    print(result)

if __name__ == "__main__":
    main()