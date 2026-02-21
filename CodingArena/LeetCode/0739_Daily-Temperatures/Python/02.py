"""
Author: Mrunal Nirajkumar Shah
Date  : 17th February, 2026

LeetCode: 739. Daily Temperature

Time Limit Exceeded
Solution Description:
Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = []

        for i in range(len(temperatures)):
            if len(answer) == 0:
                stack.append(i)
                answer.append(0)
                continue

            j = len(stack) - 1
            while j >= 0:
                if temperatures[i] > temperatures[stack[j]]:
                    answer[stack[j]] = i - stack[j]
                    j -= 1

                    stack.pop(j + 1)
                else:
                    j -= 1

            stack.append(i)
            answer.append(0)
            
                    
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